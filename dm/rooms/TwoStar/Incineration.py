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

__all__ = ("Incineration",)

################################################################################
class Incineration(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-126",
            name="Incineration",
            description=(
                "Inflicts {damage} damage and give {status} Burn to the hero "
                "that entered the room."
            ),
            level=level,
            rank=2
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.damage(self.effect_value()[0])
                unit.add_status("Burn", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect.

        A random value from the base effectiveness range is chosen, then a random
        value from the additional effectiveness range is added to the total for
        each level of this room.

        Breakdown:
        ----------
        Damage: **effect = (a to b) + ((x to y) * LV)**

        Status: **effect = n + (e * LV)**

        In these functions:

        - (a to b) is the base effectiveness.
        - (x to y) is the additional effectiveness per level.
        - n is the base number of stacks.
        - e is the additional number of stacks per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 21)
        burn = 32
        for _ in range(self.level):
            damage += random.randint(0, 20)
            burn += 16

        return damage, burn

################################################################################
