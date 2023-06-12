from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates   import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from ..core.game          import DMGame
################################################################################

__all__ = ("TreasureFate",)

################################################################################
class TreasureFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Treasure

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-10t",
            "Treasure",
            "Relics of great power await you.",
            Vector2(x, y),
            5,
            "treasure_fate"
        )

################################################################################
