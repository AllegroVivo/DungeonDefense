from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from utilities      import *
from ...core.vector import DMVector

if TYPE_CHECKING:
    from ...core.game         import DMGame
################################################################################

__all__ = ("ReadingFate",)

################################################################################
class ReadingFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Reading

    def __init__(self, game: DMGame, x: int = 3, y: int = 0):

        super().__init__(
            game,
            _id="FAT-204",
            name="Reading",
            description=(
                "Select a book to read and gain a benefit for the rest of the run."
            ),
            new_state="dng_reading",
            rank=0,
            position=DMVector(x, y)
        )

################################################################################
