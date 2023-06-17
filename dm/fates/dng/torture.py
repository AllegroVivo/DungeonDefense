from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ._base import DungeonFateCard
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("TortureFate",)

################################################################################
class TortureFate(DungeonFateCard):

    FTYPE: DMFateType = DMFateType.Torture

    def __init__(self, game: DMGame, x: int = 4, y: int = 0):

        super().__init__(
            game,
            _id="FAT-205",
            name="Torture",
            description="Select a prisoner to Torture.",
            next_state="dng_torture",
            position=Vector2(x, y)
        )

################################################################################
