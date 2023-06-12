from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.fates  import DMFateCard
from utilities      import *
from ...core.vector import DMVector

if TYPE_CHECKING:
    from ...core.game       import DMGame
################################################################################

__all__ = ("RestFate",)

################################################################################
class RestFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Rest

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            _id="FAT-201",
            name="Rest",
            description=(
                "Rest for a day and Recover 30% of your max LIFE rounded up."
            ),
            new_state="dng_rest",
            rank=0,
            position=DMVector(x, y)
        )

################################################################################
