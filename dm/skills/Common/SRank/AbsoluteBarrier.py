from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

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
            rank=4,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Select a random ally
        target = self.random.choice(ctx.room.units_of_type(self.owner))
        # Apply shield
        target.add_status("Shield", 5, self)

################################################################################
