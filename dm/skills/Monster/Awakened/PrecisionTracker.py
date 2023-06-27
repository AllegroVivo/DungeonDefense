from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PrecisionTracker",)

################################################################################
class PrecisionTracker(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-324",
            name="Precision Tracker",
            description=(
                "When an enemy in Hide state receives damage, has a 30 % chance "
                "to decrease Hide by 1. Also, the target cannot evade when a "
                "monster in Focus state attacks."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.target, (DMHero, DMMonster)):
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            if isinstance(ctx.target, DMHero):
                hide = ctx.target.get_status("Hide")
                if hide is not None:
                    if self.random.chance(30):
                        hide.reduce_stacks_by_one()
            elif isinstance(ctx.source, DMMonster):
                focus = ctx.source.get_status("Focus")
                if focus is not None:
                    if ctx.will_fail:
                        ctx._fail = False

################################################################################
