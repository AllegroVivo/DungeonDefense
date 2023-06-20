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

__all__ = ("Ignition",)

################################################################################
class Ignition(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-125",
            name="Ignition",
            description=(
                "Inflicts {value} damage to hero that entered the room. Inflict "
                "additional damage as much the hero's Burn stat."
            ),
            level=level,
            rank=2
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                damage = self.effect_value()
                burn = unit.get_status("Burn")
                if burn is not None:
                    damage += burn.stacks

                unit.damage(damage)

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

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

        damage = random.randint(1, 18)
        for _ in range(self.level):
            damage += random.randint(0, 17)

        return damage

################################################################################
