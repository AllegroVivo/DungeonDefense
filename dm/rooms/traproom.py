from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, List, Optional, Tuple

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("DMTrapRoom",)

################################################################################
class DMTrapRoom(DMRoom):

    __slots__ = (
        "_activated_before",
        "_damage_range",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        position: Vector2,
        dmg_range: Optional[Tuple[int, int]] = None,
        *,
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None
    ):

        super().__init__(state, position, _id, name, description, rank, level, unlock)

        self._activated_before: bool = False
        self._damage_range: Optional[Tuple[int, int]] = dmg_range

################################################################################
    @property
    def room_type(self) -> DMRoomType:

        return DMRoomType.Trap

################################################################################
    @property
    def activated_before(self) -> bool:

        return self._activated_before

################################################################################
    @property
    def statuses(self) -> List[DMStatus]:
        """For compatibility with :class:`AttackContext`."""

        return []

################################################################################
    def refresh_stats(self) -> None:
        """For compatibility with :class:`AttackContext`."""
        pass

################################################################################
    def activate_first_time(self) -> None:

        self._activated_before = True

################################################################################
    def _copy(self, **kwargs) -> DMTrapRoom:

        new_obj: DMTrapRoom = super()._copy(**kwargs)  # type: ignore

        new_obj._activated_before = False

        return new_obj  # type: ignore

################################################################################
