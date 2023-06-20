from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurtainOfDarkness",)

################################################################################
class CurtainOfDarkness(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-155",
            name="Curtain of Darkness",
            description=(
                "Gives {blind} Blind to heroes that entered the room. Give "
                "{defense} Defense to all monsters in adjacent rooms at the "
                "beginning of the battle."
            ),
            level=level,
            rank=4
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.add_status("Blind", self.effect_value()[0])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        blind = 1 + (1 * self.level)
        defense = 3 + (1 * self.level)

        return blind, defense

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.game.subscribe_event("battle_start", self.battle_start)

################################################################################
    def battle_start(self) -> None:

        rooms = self.game.dungeon.get_adjacent_rooms(self.position)
        for room in rooms:
            for monster in room.monsters:
                monster.add_status("Defense", self.effect_value()[0])

################################################################################
