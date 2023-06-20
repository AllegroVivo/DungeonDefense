from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Crossbow",)

################################################################################
class Crossbow(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-179",
            name="Crossbow",
            description=(
                "Once recharged, inflict {value} damage to random enemies "
                "in adjacent area."
            ),
            level=level,
            rank=5
        )

        self.setup_charging(1.0, 1.0)

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

        damage = random.randint(1, 49)
        for _ in range(self.level):
            damage += random.randint(0, 48)

        return damage

################################################################################
    def on_charge(self) -> None:

        rooms = self.game.dungeon.get_adjacent_rooms(self.position)
        heroes = []
        for room in rooms:
            heroes += room.heroes

        # No specification on how many targets, so I'm going with 3.
        targets = random.choices(heroes, k=3)
        for target in targets:
            target.damage(self.effect_value())

################################################################################
