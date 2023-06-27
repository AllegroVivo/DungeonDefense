from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Turnaround",)

################################################################################
class Turnaround(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-356",
            name="Turnaround",
            description=(
                "Transfer Fury of all enemies in the room to self when entering "
                "the Battle Room."
            ),
            rank=5,
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
                # If the enemy has Fury
                fury = unit.get_status("Fury")
                if fury:
                    # Transfer Fury to self
                    self.owner.add_status("Fury", fury.stacks, self)
                    fury.deplete_all_stacks()

################################################################################
