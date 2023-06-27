from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BladeOfDeath",)

################################################################################
class BladeOfDeath(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-276",
            name="Blade of Death",
            description=(
                "Inflict 60 (+4.0*ATK) damage to target and apply extra 15% "
                "damage per number of Immortality applied to self. Apply 3 "
                "Immortality to all monsters if this kills an enemy."
            ),
            rank=6,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=60, scalar=4.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            immortality = self.owner.get_status("Immortality")
            scalar = 1.0
            if immortality is not None:
                scalar += (0.15 * immortality.stacks)
            ctx.target.damage(self.effect * scalar)
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if not ctx.target.is_alive:
            for monster in self.game.all_monsters:
                monster.add_status("Immortality", 3, self)
