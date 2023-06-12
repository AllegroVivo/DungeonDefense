from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Bat",)

################################################################################
class Bat(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-104",
            name="Bat",
            description="A big ol' scary bat! [y]OH SHIT kill it!",
            life=40,
            attack=6,
            defense=2,
            dex=10,
            rank=1,
            idle_frames=6
        )

################################################################################
