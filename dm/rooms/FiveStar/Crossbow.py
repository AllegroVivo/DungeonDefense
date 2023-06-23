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
            rank=5,
            base_dmg=49
        )
        self.setup_charging(1.0, 1.0)

################################################################################
    def on_charge(self) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        # No specification on how many targets, so I'm going with 3.
        targets = self.random.sample(heroes, 3)
        for target in targets:
            target.damage(self.damage)

################################################################################
