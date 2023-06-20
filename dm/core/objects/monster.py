from __future__ import annotations

from typing     import TYPE_CHECKING, Optional, TypeVar

from dm.core.objects.unit import DMUnit
from ..graphics import MonsterGraphical
from utilities  import *

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.room import DMRoom
################################################################################

__all__ = ("DMMonster",)

M = TypeVar("M", bound="DMMonster")

################################################################################
class DMMonster(DMUnit):

    __slots__ = (
        "_highlighted",
        "_deployed",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        level: int,
        *,
        _id: str,
        name: str,
        description: Optional[str] = None,
        rank: int,
        unlock: Optional[UnlockPack] = None,
        life: int,
        attack: int,
        defense: float,
        idle_frames: int = 5
    ):

        super().__init__(
            state, _id, name, description, life, attack, defense, 1.0, level,
            rank=rank, unlock=unlock, graphics=MonsterGraphical(self, num_frames=idle_frames)
        )

        self._highlighted: bool = False
        self._deployed: bool = False

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Monster

################################################################################
    @property
    def highlighted(self) -> bool:

        return self.graphics._highlighted  # type: ignore

################################################################################
    def highlight(self, state: bool) -> None:

        self._graphics.toggle_highlighting(state)  # type: ignore

################################################################################
    def deploy(self, room: DMRoom) -> None:

        self.room = room
        self._deployed = True

################################################################################
    def withdraw(self) -> None:

        self._room = None
        self._deployed = False

################################################################################
