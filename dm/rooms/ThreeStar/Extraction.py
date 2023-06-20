from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Extraction",)

################################################################################
class Extraction(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-138",
            name="Extraction",
            description=(
                "Inflicts {damage} damage and collect {value} information from "
                "hero that entered the room. When 100 pieces of information are "
                "collected, a random monster is upgraded."
            ),
            level=level,
            rank=3
        )

        self._information: float = 0

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.damage(self.effect_value()[0])
                self._information += self.effect_value()[1]

        if self._information >= 100:
            self._information -= 100
            self.game.dungeon.upgrade_random_monster(include_inventory=True)

################################################################################
    def effect_value(self) -> Tuple[int, float]:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        **info = b + (a * LV)**

        In this function:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - b is the base info collected.
        - a is the additional info collected per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 3)
        collect = 1
        for _ in range(self.level):
            damage += random.randint(0, 2)
            collect += 0.5

        return damage, collect

################################################################################
