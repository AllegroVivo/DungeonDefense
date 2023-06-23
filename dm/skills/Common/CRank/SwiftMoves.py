from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwiftMoves",)

################################################################################
class SwiftMoves(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-109",
            name="Swift Moves",
            description="(Passive) Gain 1 Dodge when damage is received 4 times.",
            rank=1,
            cooldown=0,
            passive=True
        )

        self._damage_counter: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            self._damage_counter += 1

            if self._damage_counter >= 4:
                self._damage_counter = 0
                self.owner.add_status("Dodge", 1, self)

################################################################################
