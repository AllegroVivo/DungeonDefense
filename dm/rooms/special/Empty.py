from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.room import DMRoom
from utilities          import *

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("EmptyRoom",)

################################################################################
class EmptyRoom(DMRoom):

    def __init__(self, game: DMGame, row: int, col: int):

        super().__init__(
            game, row, col,
            _id="ROOM-000",
            name="Empty",
            description="There's... nothing here...",
            level=0,
            rank=0,
            unlock=None
        )

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Empty

################################################################################
