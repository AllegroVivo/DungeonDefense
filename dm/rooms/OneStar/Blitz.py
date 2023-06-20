from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Blitz",)

################################################################################
class Blitz(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-105",
            name="Blitz",
            description=(
                "Inflicts {value} damage to hero that entered the room. If hero "
                "is under the effect of Haze or Charm, 3x damage is inflicted."
            ),
            level=level,
            rank=1,
            unlock=UnlockPack.Original
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                damage = self.effect_value()

                # If the hero is under the effect of Haze or Charm, triple the damage.
                haze = unit.get_status("Haze")
                charm = unit.get_status("Charm")
                if haze or charm:
                    damage *= 3

                unit.damage(damage)

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

        damage = random.randint(1, 14)
        for _ in range(self.level):
            damage += random.randint(0, 14)

        return damage

################################################################################
