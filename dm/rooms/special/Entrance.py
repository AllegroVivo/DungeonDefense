from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.room import DMRoom
from utilities          import *

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("EntranceRoom",)

################################################################################
class EntranceRoom(DMRoom):

    def __init__(self, game: DMGame, row: int, col: int):

        super().__init__(
            game, row, col,
            _id="ENTR-000",
            name="Entrance",
            description="An entryway into to the dungeon.",
            rank=0,
            level=0,
            unlock=None
        )

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Entrance

################################################################################
