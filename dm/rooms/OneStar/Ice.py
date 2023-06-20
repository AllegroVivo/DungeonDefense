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

__all__ = ("Ice",)

################################################################################
class Ice(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-107",
            name="Ice",
            description=(
                "Inflicts {damage} damage and give {status} Slow to each hero "
                "that enters the room."
            ),
            level=level,
            rank=1
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.damage(self.effect_value()[0])
                unit.add_status("Slow", self.effect_value()[1])

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

        damage = random.randint(1, 10)
        slow = 2
        for _ in range(self.level):
            damage += random.randint(0, 9)
            slow += 1

        return damage, slow

################################################################################
