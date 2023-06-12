from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates   import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("EquipmentTraderFate",)

################################################################################
class EquipmentTraderFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.EquipmentTrader

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-110",
            "Equipment Trader",
            "Buy, Sell, and swap monster equipment.",
            Vector2(x, y),
            4,
            "equipment_trader"
        )

################################################################################
