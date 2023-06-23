from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DefenseCaptain",)

################################################################################
class DefenseCaptain(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-123",
            name="Defense Captain",
            description=(
                "Apply 3 Defense to all allies in the room for every 2 "
                "attacks received."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

        self._atk_count: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            self._atk_count += 1

        if self._atk_count % 2 == 0:
            for unit in ctx.room.units_of_type(self.owner):
                unit.add_status("Defense", 3, self)

################################################################################
