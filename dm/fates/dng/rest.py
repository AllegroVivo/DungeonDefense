from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ._base import DungeonFateCard
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("RestFate",)

################################################################################
class RestFate(DungeonFateCard):

    FTYPE: DMFateType = DMFateType.Rest

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            _id="FAT-201",
            name="Rest",
            description=(
                "Rest for a day and Recover 30% of your max LIFE rounded up."
            ),
            next_state="dng_rest",
            position=Vector2(x, y)
        )

################################################################################
