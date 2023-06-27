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

__all__ = ("InfiniteWeb",)

################################################################################
class InfiniteWeb(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-306",
            name="Infinite Web",
            description=(
                "Enemy in the dungeon receives 1 Web each time it takes damage."
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
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            ctx.target.add_status("Web", 1, self)
