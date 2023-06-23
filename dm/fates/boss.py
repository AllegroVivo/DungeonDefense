from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates.fatecard  import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("BossFate",)

################################################################################
class BossFate(DMFateCard):

    FTYPE: FateType = FateType.Boss

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-104",
            "Boss Battle",
            "An incredibly powerful band of heroes is approaching.",
            Vector2(x, y),
            0,
            "boss_battle"
        )

################################################################################
