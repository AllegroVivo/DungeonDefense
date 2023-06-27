from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AccelerationSkill",)

################################################################################
class AccelerationSkill(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-112",
            name="Acceleration",
            description="Apply 4 Acceleration to ally.",
            rank=3,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Select random ally in the room.
        target = self.random.choice(ctx.room.units_of_type(self.owner))
        # Apply Acceleration.
        target.add_status("Acceleration", 4, self)

################################################################################
