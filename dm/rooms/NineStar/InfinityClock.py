from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("InfinityClock",)

################################################################################
class InfinityClock(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-225",
            name="Infinity Clock",
            description=(
                "Boost DEX of monsters in adjacent rooms by {value} %, and "
                "when hero enters, give {status} Acceleration to monsters in "
                "adjacent rooms."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            monsters = []
            for room in self.adjacent_rooms:
                monsters.extend(room.monsters)

            for monster in monsters:
                monster.add_status("Acceleration", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[float, int]:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        stat = (100 + (4 * self.level)) / 100  # Convert to percentage
        status = 5 + (1 * self.level)

        return stat, status

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("room_enter")

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.increase_stat_pct("DEX", self.effect_value()[0])

################################################################################
