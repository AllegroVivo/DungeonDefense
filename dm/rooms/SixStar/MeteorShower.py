from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MeteorShower",)

################################################################################
class MeteorShower(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-199",
            name="Meteor Shower",
            description=(
                "Inflicts 1~49 (+0~48 per Lv) damage and gives 128 (+96 per Lv) Burn to all heroes in adjacent rooms when a hero enters the room. Damage inflicted is doubled for enemies under the effect of Slow."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        pass

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

        damage = random.randint(1, 49)
        status = 128
        for _ in range(self.level):
            damage += random.randint(0, 48)
            status += 96

        return damage, status

################################################################################
