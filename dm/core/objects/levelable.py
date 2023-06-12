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
        "level",
        "experience",
        "upgrades",
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

        self.level: int = level
        self.experience: int = 0
        self.upgrades: int = upgrades

################################################################################
    def grant_exp(self, amount: int) -> None:

        self.experience += amount
        self.check_level_up()

################################################################################
    def upgrade(self) -> None:

        self.upgrades += 1

################################################################################
    def check_level_up(self) -> None:

        pass

################################################################################
    def level_up(self, num_levels: int = 1) -> None:

        self.level += num_levels
        self.experience = 0

################################################################################
