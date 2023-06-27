from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ExplosiveBrand",)

################################################################################
class ExplosiveBrand(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-315",
            name="Explosive Brand",
            description=(
                "When an enemy is damaged in the dungeon, spend 10 % of the "
                "Burn stat to deal 1000 % of the spent stat as extra damage."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.target, DMHero):
            ctx.register_post_execute(self.callback)

################################################################################
    @staticmethod
    def callback(ctx: AttackContext) -> None:

        if ctx.damage > 0:
            burn = ctx.target.get_status("Burn")
            if burn is not None:
                effect_amt = int(burn.stacks * 0.10)
                burn.reduce_stacks_flat(effect_amt)
                ctx.amplify_flat(effect_amt * 10)  # 1000%

################################################################################
