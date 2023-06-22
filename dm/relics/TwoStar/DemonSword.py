from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonSword",)

################################################################################
class DemonSword(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-141",
            name="Demon Sword",
            description=(
                "All monsters' ATK is increased by 20% for every Shrine "
                "placed in the dungeon."
            ),
            rank=2
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        # If there are no shrines placed, exit.
        if self.effect_value() == -1:
            return

        # Apply Attack buff to all monsters.
        for monster in self.game.deployed_monsters:
            monster.increase_stat_pct("atk", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        # Loop through all rooms and count the shrines.
        shrines = 0
        for room in self.game.all_rooms():
            if room.room_type is RoomType.Shrine:
                shrines += 1

        # Return a flag if there are no shrines.
        if shrines == 0:
            return -1

        return 0.15

################################################################################
