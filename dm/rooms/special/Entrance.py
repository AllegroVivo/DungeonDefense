from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ...core.objects.room   import DMRoom
from utilities              import *

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("EntranceRoom",)

################################################################################
class EntranceRoom(DMRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None):

        super().__init__(
            game, position or Vector2(5, 1),
            _id="ENTR-000",
            name="Entrance",
            description="An entryway into to the dungeon.",
            rank=0,
            level=0,
            unlock=None,
            effects=None,
            base_dmg=None,
        )

################################################################################
    @property
    def room_type(self) -> RoomType:

        return RoomType.Entrance

################################################################################
