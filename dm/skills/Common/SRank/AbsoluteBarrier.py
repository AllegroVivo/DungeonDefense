from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AbsoluteBarrier",)

################################################################################
class AbsoluteBarrier(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-173",
            name="Absolute Barrier",
            description=(
                "Apply 5 Shield to ally."
            ),
            rank=2,
            cooldown=2
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        target = self.random.choice(ctx.room.units_of_type(self.owner))
        target.add_status("Shield", 5, self)

################################################################################
