from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicBarrier",)

################################################################################
class MagicBarrier(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-181",
            name="Magic Barrier",
            description=(
                "Apply 3 Shield to all allies in the room."
            ),
            rank=2,
            cooldown=4
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in ctx.room.units_of_type(self.owner):
            unit.add_status("Shield", 3, self)

################################################################################
