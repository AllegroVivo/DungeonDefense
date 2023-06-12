from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Lizardman",)

################################################################################
class Lizardman(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-109",
            name="Lizardman",
            life=95,
            attack=9,
            defense=3.75,
            rank=2,
            dex=10
        )

################################################################################
