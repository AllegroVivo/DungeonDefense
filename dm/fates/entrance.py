from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates.fatecard  import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("EntranceFate",)

################################################################################
class EntranceFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Entrance

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "ENTR-101",
            "Entrance",
            "Entrypoint to this Fate cycle",
            Vector2(x, y),
            0,
            "<null>"
        )

################################################################################
