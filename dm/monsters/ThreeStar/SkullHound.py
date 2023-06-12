from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("SkullHound",)

################################################################################
class SkullHound(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-139",
            name="Skull Hound",
            life=120,
            attack=16,
            defense=12,
            rank=3,
            dex=10,
            unlock=UnlockPack.Original
        )

################################################################################
