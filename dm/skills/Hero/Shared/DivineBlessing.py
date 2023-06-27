from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DivineBlessing",)

################################################################################
class DivineBlessing(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-338",
            name="Divine Blessing",
            description=(
                "Apply 1 Quick, 1 Acceleration, 1 Shield, and 1 Focus to allies."
            ),
            rank=5,
            cooldown=CooldownType.RoomWide
        )

        # The description doesn't mention *which allies, so I'm making an
        # assumption that it's all allies in the room.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each ally in the room
        for unit in self.room.units_of_type(self.owner):
            # Apply the statuses
            for status in ("Quick", "Acceleration", "Shield", "Focus"):
                unit.add_status(status, 1, self)

################################################################################
