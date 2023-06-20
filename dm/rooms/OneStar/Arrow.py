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

__all__ = ("Arrow",)

################################################################################
class Arrow(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-104",
            name="Arrow",
            description=(
                "Inflicts {damage} damage to each hero that enters the room."
            ),
            level=level,
            rank=1
        )

################################################################################
    def activate(self, unit: DMUnit) -> None:
        """A general event response function."""

        self.attack(unit)

################################################################################
    def effect_value(self) -> Tuple[int]:
        """The value of this room's effect.

        A random value from the base effectiveness range is chosen, then a random
        value from the additional effectiveness range is added to the total for
        each level of this room.

        Breakdown:
        ----------
        **effect = (a to b) + ((x to y) * LV)**

        In this function:

        - (a to b) is the base effectiveness.
        - (x to y) is the additional effectiveness per level.
        - LV is the level of this room.
        """

        effect = random.randint(1, 18)
        for _ in range(self.level):
            effect += random.randint(0, 17)

        return effect,

################################################################################
    def activate(self, unit: DMHero) -> None:
        """Called automatically when a unit enteres this room."""

        pass

################################################################################
