from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from utilities      import *
from ...core.vector import DMVector

if TYPE_CHECKING:
    from ...core.game         import DMGame
################################################################################

__all__ = ("UpgradeFate",)

################################################################################
class UpgradeFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Upgrade

    def __init__(self, game: DMGame, x: int = 1, y: int = 0):

        super().__init__(
            game,
            _id="FAT-202",
            name="Upgrade",
            description="Select a room to Upgrade.",
            new_state="dng_upgrade",
            rank=0,
            position=DMVector(x, y)
        )

################################################################################
