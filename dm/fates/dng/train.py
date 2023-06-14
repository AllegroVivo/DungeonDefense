from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from utilities      import *
from ...core.vector import DMVector

if TYPE_CHECKING:
    from ...core.game         import DMGame
################################################################################

__all__ = ("TrainFate",)

################################################################################
class TrainFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Train

    def __init__(self, game: DMGame, x: int = 2, y: int = 0):

        super().__init__(
            game,
            _id="FAT-203",
            name="Train",
            description="Select a monster to promote to Elite and beyond.",
            new_state="dng_train",
            rank=0,
            position=DMVector(x, y)
        )

################################################################################
