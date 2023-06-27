from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MassAccel",)

################################################################################
class MassAccel(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-162",
            name="Mass Accel",
            description=(
                "Apply 2 Acceleration to all allies in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each ally in the room
        for unit in ctx.room.units_of_type(self.owner):
            # Apply Acceleration.
            unit.add_status("Acceleration", 2, self)

################################################################################
