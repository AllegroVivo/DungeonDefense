from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ArrowBomb",)

################################################################################
class ArrowBomb(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-211",
            name="Arrow Bomb",
            description=(
                "Once recharged, inflict {value} damage to all enemies in "
                "adjacent area."
            ),
            level=level,
            rank=7,
            unlock=UnlockPack.Myth
        )

        self.setup_charging(1.6, 1.6)

################################################################################
    def on_charge(self) -> None:

        pass

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

        damage = random.randint(1, 33)
        for _ in range(self.level):
            damage += random.randint(0, 32)

        return damage

################################################################################
