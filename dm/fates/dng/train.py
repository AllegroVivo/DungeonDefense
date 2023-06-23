from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ._base import DungeonFateCard
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("TrainFate",)

################################################################################
class TrainFate(DungeonFateCard):

    FTYPE: FateType = FateType.Train

    def __init__(self, game: DMGame, x: int = 2, y: int = 0):

        super().__init__(
            game,
            _id="FAT-203",
            name="Train",
            description="Select a monster to promote to Elite and beyond.",
            next_state="dng_train",
            position=Vector2(x, y)
        )

################################################################################
