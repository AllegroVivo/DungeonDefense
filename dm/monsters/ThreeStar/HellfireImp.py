from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("HellfireImp",)

################################################################################
class HellfireImp(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):
        super().__init__(
            game,
            level,
            _id="MON-138",
            name="Hellfire Imp",
            life=110,
            attack=20,
            defense=9,
            rank=3,
            dex=10,
            unlock=UnlockPack.Original,
            idle_frames=6
        )

################################################################################
