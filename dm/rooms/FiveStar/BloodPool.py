from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BloodPool",)

################################################################################
class BloodPool(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-172",
            name="Blood Pool",
            description=(
                "Give {value} Vampire and Fury to all monsters in adjacent "
                "rooms whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                rooms = self.game.dungeon.get_adjacent_rooms(self.position)
                for room in rooms:
                    for monster in room.monsters:
                        monster.add_status("Vampire", self.effect_value())
                        monster.add_status("Fury", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 20 + (12 * self.level)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("room_enter")

################################################################################
