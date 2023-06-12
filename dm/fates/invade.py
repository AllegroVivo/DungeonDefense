from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ..core.fates   import DMFateCard
from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("InvadeFate",)

################################################################################
class InvadeFate(DMFateCard):

    FTYPE: DMFateType = DMFateType.Invade

    def __init__(self, game: DMGame, x: int = 0, y: int = 0):

        super().__init__(
            game,
            "FAT-103",
            "Invade Battle",
            "Boss! We found one of the heroes' bases. Let's take the battle to them!",
            Vector2(x, y),
            3,
            "invade_battle"
        )

################################################################################
