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

__all__ = ("Multishot",)

################################################################################
class Multishot(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-160",
            name="Multishot",
            description=(
                "Inflicts {value} damage to 3 enemies in this room when a "
                "hero enters the room."
            ),
            level=level,
            rank=4
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                targets = random.choices(self.heroes, k=3)
                for target in targets:
                    target.damage(self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        A random value from the base damage range is chosen, then a random value
        from the additional damage range is added to the total for each level of
        this room.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        In this function:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 34)
        for _ in range(self.level):
            damage += random.randint(0, 33)

        return damage

################################################################################