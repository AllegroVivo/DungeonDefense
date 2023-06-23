from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Extraction",)

################################################################################
class Extraction(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-138",
            name="Extraction",
            description=(
                "Inflicts {damage} damage and collect {value} information from "
                "hero that entered the room. When 100 pieces of information are "
                "collected, a random monster is upgraded."
            ),
            level=level,
            rank=3,
            base_dmg=3,
            effects=[
                Effect(name="Information", base=1, per_lv=1),
            ]
        )

        self._information: float = 0

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)

        self._information += self.effects["Information"]
        if self._information >= 100:
            self._information -= 100
            self.game.dungeon.upgrade_random_monster(include_inventory=True)

################################################################################
