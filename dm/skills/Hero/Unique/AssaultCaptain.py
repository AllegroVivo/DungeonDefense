from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AssaultCaptain",)

################################################################################
class AssaultCaptain(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-348",
            name="Assault Captain",
            description=(
                "Apply 2 Stun to all enemies in the room when entering the "
                "Battle Room."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # For each enemy in the room
            for unit in unit.room.units_of_type(self.owner, inverse=True):
                # Apply Stun.
                unit.add_status("Stun", 2, self)

################################################################################
