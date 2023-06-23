from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates.fatecard  import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from ..core.game          import DMGame
################################################################################

__all__ = ("TrialFate",)

################################################################################
class TrialFate(DMFateCard):

    FTYPE: FateType = FateType.Trial

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-111",
            "Trial",
            "Take on an extra challenge... if you dare.",
            Vector2(x, y),
            5,
            "trial_fate"
        )

################################################################################
