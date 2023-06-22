from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, TypeVar

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DMFacilityRoom",)

F = TypeVar("F", bound="DMFacilityRoom")

################################################################################
class DMFacilityRoom(DMRoom):

    __slots__ = (

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

################################################################################
    @property
    def room_type(self) -> RoomType:

        return RoomType.Facility

################################################################################
    def _copy(self, **kwargs) -> DMFacilityRoom:

        new_obj: Type[F] = super()._copy(**kwargs)  # type: ignore

        return new_obj  # type: ignore

################################################################################
