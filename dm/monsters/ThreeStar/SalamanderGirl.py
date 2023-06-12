from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("SalamanderGirl",)

################################################################################
class SalamanderGirl(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-123",
            name="Salamander Girl",
            life=95,
            attack=16,
            defense=6.75,
            rank=3,
            dex=10
        )

################################################################################
