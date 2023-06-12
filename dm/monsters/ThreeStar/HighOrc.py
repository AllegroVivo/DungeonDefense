from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("HighOrc",)

################################################################################
class HighOrc(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-130",
            name="High Orc",
            life=120,
            attack=15,
            defense=6,
            rank=3,
            dex=10,
        )

################################################################################
