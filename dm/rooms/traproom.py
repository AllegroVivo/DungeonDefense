from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, List, Optional, TypeVar

from dm.core.objects.room import DMRoom
from utilities      import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("DMTrapRoom",)

R = TypeVar("R")

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
        _id: str,
        name: str,
        description: str,
        rank: int,
        level: int = 1,
        unlock: Optional[UnlockPack] = None,
    ):

        super().__init__(state, position, _id, name, description, rank, level, unlock)

        self._activated_before: bool = False

        # Subscribe to room enter events since those are most likely to trigger traps.
        self.listen("room_enter")

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
    def attack(self, unit: DMUnit) -> None:

        self.game.battle_mgr.trap_attack(self, unit)

################################################################################
    def activate(self, unit: DMUnit) -> None:
        """A general event response function."""

        pass

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # This is where the automatic listener call goes to.
        if unit.room == self:
            self.activate(unit)

################################################################################
    def _copy(self, **kwargs) -> DMTrapRoom:

        new_obj: DMTrapRoom = super()._copy(**kwargs)  # type: ignore

        new_obj._activated_before = False

        return new_obj  # type: ignore

################################################################################
