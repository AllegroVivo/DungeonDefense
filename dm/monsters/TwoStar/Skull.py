from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Skull",)

################################################################################
class Skull(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-106",
            name="Skull",
            life=70,
            attack=10,
            defense=4.0,
            rank=2,
            dex=10
        )

################################################################################
