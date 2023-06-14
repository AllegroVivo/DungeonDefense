from __future__ import annotations

from typing     import TYPE_CHECKING, Optional, TypeVar

from dm.core.objects.unit import DMUnit
from ..graphics import MonsterGraphical
from utilities  import *

if TYPE_CHECKING:
    from dm.core.game import DMGame
################################################################################

__all__ = ("DMMonster",)

M = TypeVar("M", bound="DMMonster")

################################################################################
class DMMonster(DMUnit):

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
        dex: float,
        idle_frames: int = 5
    ):

        super().__init__(
            state, _id, name, description, life, attack, defense, dex, level,
            rank=rank, unlock=unlock, graphics=MonsterGraphical(self, num_frames=idle_frames)
        )

################################################################################
