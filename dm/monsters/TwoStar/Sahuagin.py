from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Sahuagin",)

################################################################################
class Sahuagin(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-114",
            name="Sahuagin",
            life=60,
            attack=11,
            defense=4.5,
            rank=2,
            dex=10
        )

################################################################################
