from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Ogre",)

################################################################################
class Ogre(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-136",
            name="Ogre",
            life=150,
            attack=13,
            defense=5,
            rank=3,
            dex=10
        )

################################################################################
