from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Zombie",)

################################################################################
class Zombie(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-107",
            name="Zombie",
            life=90,
            attack=9,
            defense=5.0,
            rank=2,
            dex=10,
            idle_frames=6
        )

################################################################################
