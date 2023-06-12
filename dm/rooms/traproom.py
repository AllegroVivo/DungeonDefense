from __future__ import annotations

from typing     import TYPE_CHECKING, List, Optional, TypeVar

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from pygame     import Surface

    from dm.core    import DMGame, DMMonster
################################################################################

__all__ = ("DMTrapRoom",)

R = TypeVar("R")

################################################################################
class DMTrapRoom(DMRoom):

    __slots__ = (

    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        row: int,
        col: int,
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None,
    ):

        super().__init__(state, row, col, _id, name, description, rank, level, unlock)

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Trap

################################################################################
    def draw(self, screen: Surface) -> None:

        super().draw(screen)

################################################################################
    def _copy(self, **kwargs) -> DMTrapRoom:

        new_obj: DMTrapRoom = super()._copy(**kwargs)  # type: ignore

        return new_obj  # type: ignore

################################################################################
