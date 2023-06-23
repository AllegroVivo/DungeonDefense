from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ._base import DungeonFateCard
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("RoomSwapFate",)

################################################################################
class RoomSwapFate(DungeonFateCard):

    FTYPE: FateType = FateType.RoomSwap

    def __init__(self, game: DMGame, x: int = 5, y: int = 0):

        super().__init__(
            game,
            _id="FAT-206",
            name="Room Swap",
            description="Select two rooms and switch their locations.",
            next_state="dng_roomswap",
            position=Vector2(x, y)
        )

################################################################################
