from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Meteor",)

################################################################################
class Meteor(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-180",
            name="Meteor",
            description=(
                "Inflicts {damage} damage and gives {status} Burn to all heroes "
                "in the room when a hero enters the room. Damage inflicted is "
                "doubled for enemies under the effect of Slow."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original
        ),

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            for hero in self.heroes:
                damage = self.effect_value()[0]
                if unit.get_status("Slow") is not None:
                    damage *= 2

                hero.damage(damage)
                hero.add_status("Burn", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect(s).

        A random value from the base damage range is chosen, then a random value
        from the additional damage range is added to the total for each level of
        this room.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        **status = b + (a * LV)**

        In these functions:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - b is the base status.
        - a is the additional stacks per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 31)
        status = 32
        for _ in range(self.level):
            damage += random.randint(0, 30)
            status += 24

        return damage, status

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        pass

################################################################################
