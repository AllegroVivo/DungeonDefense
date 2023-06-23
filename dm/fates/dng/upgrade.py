from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING

from ._base import DungeonFateCard
from utilities      import *

if TYPE_CHECKING:
    from ...core.game.game import DMGame
################################################################################

__all__ = ("UpgradeFate",)

################################################################################
class UpgradeFate(DungeonFateCard):

    FTYPE: FateType = FateType.Upgrade

    def __init__(self, game: DMGame, x: int = 1, y: int = 0):

        super().__init__(
            game,
            _id="FAT-202",
            name="Upgrade",
            description="Select a room to Upgrade.",
            next_state="dng_upgrade",
            position=Vector2(x, y)
        )

################################################################################
