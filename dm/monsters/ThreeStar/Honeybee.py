from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Honeybee",)

################################################################################
class Honeybee(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-140",
            name="Honeybee",
            life=130,
            attack=15,
            defense=12,
            rank=3,
            dex=10,
            unlock=UnlockPack.Original
        )

################################################################################
