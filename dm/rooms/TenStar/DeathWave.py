from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeathWave",)

################################################################################
class DeathWave(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-237",
            name="Death Wave",
            description=(
                "Once recharged, give {value} Poison and {value} Corpse "
                "Explosion to all enemies in the dungeon."
            ),
            level=level,
            rank=10,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(6.6, 3.3)

################################################################################
    def on_charge(self) -> None:

        for hero in self.game.all_heroes:
            hero.add_status("Slow", self.effect_value())
            hero.add_status("Corpse Explosion", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **status = b + (a * LV)**

        In this function:

        - b is the base status.
        - a is the additional stacks per level.
        - LV is the level of this room.
        """

        return 80 + (40 * self.level)

################################################################################
