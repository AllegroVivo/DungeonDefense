from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates.fatecard  import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("EliteFate",)

################################################################################
class EliteFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Elite

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-102",
            "Elite Battle",
            "A very strong band of heroes is approaching.",
            Vector2(x, y),
            2,
            "elite_battle"
        )

################################################################################
