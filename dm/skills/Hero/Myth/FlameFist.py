from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FlameFist",)

################################################################################
class FlameFist(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-392",
            name="Flame Fist",
            description=(
                "Normal attack targets all enemies in the current room. "
                "Applies 100 (+5.0*ATK) Burn and 1 Living Bomb each time the "
                "enemy is damaged. Changes Burn applied to self to Regeneration."
            ),
            rank=9,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=100, scalar=5.0)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Register all enemies in the room as additional targets
            for unit in self.game.units_of_type(self.owner, inverse=True):
                ctx.register_additional_target(unit)
            # And wait for damage
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if not ctx.will_fail:
            # Apply Burn and Living Bomb
            ctx.target.add_status("Burn", self.effect, self)
            ctx.target.add_status("Living Bomb", 1, self)

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the target of a status
        if self.owner == ctx.target:
            # If the status is Burn
            if ctx.status.name == "Burn":
                # Give ourselves Regeneration instead
                self.owner.add_status("Regeneration", ctx.status.stacks, self)
                # And fail the application of Burn
                ctx.will_fail = True

################################################################################
