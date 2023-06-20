from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("DarkSlime",)

################################################################################
class DarkSlime(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-105",
            name="Dark Slime",
            life=90,
            attack=11,
            defense=4.0,
            rank=2,
            idle_frames=6
        )

################################################################################
