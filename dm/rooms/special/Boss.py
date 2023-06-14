from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ...rooms.battleroom    import DMBattleRoom
from utilities              import *

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("BossRoom",)

################################################################################
class BossRoom(DMBattleRoom):

    __slots__ = (
        "dark_lord",
    )

################################################################################
    def __init__(self, game: DMGame, position: Optional[Vector2] = None):

        super().__init__(
            game, position or Vector2(0, 1),
            _id="BOSS-000",
            name="Boss Chamber",
            description="The Dungeon Boss awaits the intruders...",
            rank=0,
            level=0,
            unlock=None
        )

        self.dark_lord = None

################################################################################
    def _init_dark_lord(self) -> None:

        self.dark_lord = self.game.dark_lord
        self.monsters.append(self.dark_lord)  # type: ignore

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Boss

################################################################################
