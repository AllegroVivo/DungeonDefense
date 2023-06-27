from __future__ import annotations

from typing     import TYPE_CHECKING, Optional
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SacredJewel",)

################################################################################
class SacredJewel(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-385",
            name="Sacred Jewel",
            description=(
                "Deals 200 (+2.0*ATK) damage to all enemies in the dungeon and "
                "changes Immortality possessed by the target to Curse. Bestows a "
                "curse to the enemy that killed you, and changes the Immortality "
                "gained by the target to Curse. (Also starts with 10 Immortality.)"
            ),
            rank=8,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=200, scalar=2.0)
        )

        self._curse_target: Optional[DMUnit] = None

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.game.units_of_type(self.owner, inverse=True):
            unit.damage(self.effect)
            immortality = unit.get_status("Immortality")
            if immortality is not None:
                immortality.deplete_all_stacks()
                unit.add_status("Curse", immortality.stacks, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn", self.hero_spawn)
        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # if we've died, curse the unit that killed us
        if self.owner == ctx.target:
            self._curse_target = ctx.source
            self.listen("status_applied", self.status_applied)

################################################################################
    def hero_spawn(self, unit: DMUnit) -> None:

        # If we've spawned, add 10 Immortality
        if self.owner == unit:
            self.owner.add_status("Immortality", 10, self)

################################################################################
    def status_applied(self, ctx: StatusApplicationContext) -> None:

        # If a status is applied to the unit that killed us
        if ctx.target == self._curse_target:
            # If the status is Immortality
            if ctx.status.name == "Immortality":
                # Nullify Immortality and add Curse instead
                ctx.status.deplete_all_stacks()
                self._curse_target.add_status("Curse", ctx.status.stacks, self)

################################################################################
