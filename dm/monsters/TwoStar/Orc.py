from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Orc",)

################################################################################
class Orc(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-111",
            name="Orc",
            life=85,
            attack=10,
            defense=3.75,
            rank=2,
            dex=10
        )

################################################################################
