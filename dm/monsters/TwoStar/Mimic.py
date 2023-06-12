from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Mimic",)

################################################################################
class Mimic(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-115",
            name="Mimic",
            life=110,
            attack=8,
            defense=3.5,
            rank=2,
            dex=10
        )

################################################################################
