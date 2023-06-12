from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates   import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("MonsterTraderFate",)

################################################################################
class MonsterTraderFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.MonsterTrader

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-108",
            "Monster Trader",
            "Buy, Fuse, and Upgrade monsters in the dungeon and your inventory.",
            Vector2(x, y),
            4,
            "monster_trader"
        )

################################################################################
