from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates.fatecard  import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("DungeonFate",)

################################################################################
class DungeonFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Dungeon

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-105",
            "Dungeon",
            "Perform dungeon maintenance and upgrades.",
            Vector2(x, y),
            3,
            "dungeon_fate"
        )

################################################################################
