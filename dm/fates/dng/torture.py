from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from utilities      import *
from ...core.vector import DMVector

if TYPE_CHECKING:
    from ...core.game         import DMGame
################################################################################

__all__ = ("TortureFate",)

################################################################################
class TortureFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Torture

    def __init__(self, game: DMGame, x: int = 4, y: int = 0):

        super().__init__(
            game,
            _id="FAT-205",
            name="Torture",
            description="Select a prisoner to Torture.",
            new_state="dng_torture",
            rank=0,
            position=DMVector(x, y)
        )

################################################################################
