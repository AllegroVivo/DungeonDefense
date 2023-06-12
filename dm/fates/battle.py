from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates   import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("BattleFate", )

################################################################################
class BattleFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Battle

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-101",
            "Battle",
            "A band of heroes is approaching.",
            Vector2(x, y),
            1,
            "battle"
        )

################################################################################
