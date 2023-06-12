from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("GoblinGirl",)

################################################################################
class GoblinGirl(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):
        super().__init__(
            game,
            level,
            _id="MON-118",
            name="Goblin Girl",
            life=80,
            attack=17,
            defense=7,
            rank=3,
            dex=10
        )

################################################################################
