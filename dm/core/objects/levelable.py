from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.object import DMObject
from utilities  import *

if TYPE_CHECKING:
    from dm.core.game import DMGame
################################################################################

__all__ = ("DMLevelable",)

################################################################################
class DMLevelable(DMObject):

    __slots__ = (
        "_level",
        "_exp",
        "_upgrades",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        _id: str,
        name: str,
        description: Optional[str],
        level: int,
        rank: int = 0,
        upgrades: int = 0,
        unlock: Optional[UnlockPack] = None
    ):

        super().__init__(state, _id, name, description, rank, unlock)

        self._level: int = level
        self._exp: int = 0
        self._upgrades: int = upgrades

################################################################################
    @property
    def level(self) -> int:

        return self._level

################################################################################
    @property
    def experience(self) -> int:

        return self._exp

################################################################################
    @property
    def upgrades(self) -> int:

        return self._upgrades

################################################################################
    def grant_exp(self, amount: int) -> None:

        self._exp += amount
        self.check_level_up()

################################################################################
    def upgrade(self) -> None:

        self._upgrades += 1

################################################################################
    def check_level_up(self) -> None:

        pass

################################################################################
    def level_up(self, num_levels: int = 1) -> None:

        self._level += num_levels
        self.exp = 0

################################################################################
