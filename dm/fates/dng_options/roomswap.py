from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from utilities      import *
from ...core.vector import DMVector

if TYPE_CHECKING:
    from ...core.game         import DMGame
################################################################################

__all__ = ("RoomSwapFate",)

################################################################################
class RoomSwapFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.RoomSwap

    def __init__(self, game: DMGame, x: int = 5, y: int = 0):

        super().__init__(
            game,
            _id="FAT-206",
            name="Room Exchange",
            description="Select two rooms and switch their locations.",
            new_state="dng_roomswap",
            rank=0,
            position=DMVector(x, y)
        )

################################################################################
