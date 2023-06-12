from __future__ import annotations
from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates   import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("EventFate",)

################################################################################
class EventFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Event

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-106",
            "Event",
            "Participate in a randomly selected event.",
            Vector2(x, y),
            3,
            "event_fate"
        )

################################################################################
