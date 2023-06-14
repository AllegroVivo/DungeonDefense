from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates.fatecard  import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("FacilityTraderFate",)

################################################################################
class FacilityTraderFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.FacilityTrader

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-109",
            "Facility Trader",
            "Buy, Fuse, and Upgrade rooms in the dungeon.",
            Vector2(x, y),
            4,
            "facility_trader"
        )

################################################################################
