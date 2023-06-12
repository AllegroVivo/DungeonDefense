from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Mummy",)

################################################################################
class Mummy(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-129",
            name="Mummy",
            life=110,
            attack=15,
            defense=9,
            rank=3,
            dex=10
        )

################################################################################
