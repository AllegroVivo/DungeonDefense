from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ...core.objects.room   import DMRoom
from utilities              import *

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("EmptyRoom",)

################################################################################
class EmptyRoom(DMRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None):

        super().__init__(
            game, position or Vector2(-1, -1),
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
