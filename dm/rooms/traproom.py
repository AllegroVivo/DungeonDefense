from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Dict, List, Optional, Tuple

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("DMTrapRoom",)

################################################################################
class DMTrapRoom(DMRoom):

    __slots__ = (
        "_activated_before",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        position: Vector2,
        *,
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None,
        base_dmg: Optional[int] = None,
        effects: Optional[List[Effect]] = None,
    ):

        super().__init__(
            state, position, effects, base_dmg, _id, name, description, rank, level, unlock
        )

        self._activated_before: bool = False

################################################################################
    @property
    def room_type(self) -> RoomType:

        return RoomType.Trap

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
    def activate_first_time(self) -> None:

        self._activated_before = True

################################################################################
    def reactivate(self) -> None:

        # Basically set the charge to immediately trigger when it's incremented next.
        self._current_charge = self._max_charge - 0.01

################################################################################
    def _copy(self, **kwargs) -> DMTrapRoom:

        new_obj: DMTrapRoom = super()._copy(**kwargs)  # type: ignore

        new_obj._activated_before = False

        return new_obj  # type: ignore

################################################################################
