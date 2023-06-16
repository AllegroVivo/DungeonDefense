from __future__ import annotations

from pygame     import Vector2
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
        "_activated_first_time",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        position: Vector2,
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None,
    ):

        super().__init__(state, position, _id, name, description, rank, level, unlock)

        self._activated_first_time: bool = False

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Trap

################################################################################
    @property
    def activated_for_the_first_time(self) -> bool:

        return self._activated_first_time

################################################################################
    def draw(self, screen: Surface) -> None:

        super().draw(screen)

################################################################################
    def _copy(self, **kwargs) -> DMTrapRoom:

        new_obj: DMTrapRoom = super()._copy(**kwargs)  # type: ignore

        return new_obj  # type: ignore

################################################################################
