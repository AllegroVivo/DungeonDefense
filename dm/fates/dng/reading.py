from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ._base import DungeonFateCard
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("ReadingFate",)

################################################################################
class ReadingFate(DungeonFateCard):

    FTYPE: DMFateType = DMFateType.Reading

    def __init__(self, game: DMGame, x: int = 3, y: int = 0):

        super().__init__(
            game,
            _id="FAT-204",
            name="Reading",
            description=(
                "Select a book to read and gain a benefit for the rest of the run."
            ),
            next_state="dng_reading",
            position=Vector2(x, y)
        )

################################################################################
