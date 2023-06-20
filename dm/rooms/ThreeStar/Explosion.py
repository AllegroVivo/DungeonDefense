from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Explosion",)

################################################################################
class Explosion(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-137",
            name="Explosion",
            description=(
                "Inflicts {value} damage to all enemies in the current room "
                "and all adjacent rooms when a hero enters the room."
            ),
            level=level,
            rank=3
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                heroes = []
                # Grab affected rooms
                rooms = self.game.dungeon.get_adjacent_rooms(self.position, include_current=True)
                # And compile a list of heroes in those rooms
                for room in rooms:
                    heroes += room.heroes
                # Deal damage to all heroes in the affected rooms
                for hero in heroes:
                    hero.damage(self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        A random value from the base effectiveness range is chosen, then a random
        value from the additional effectiveness range is added to the total for
        each level of this room.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        In these functions:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 6)
        for _ in range(self.level):
            damage += random.randint(0, 6)

        return damage

################################################################################
