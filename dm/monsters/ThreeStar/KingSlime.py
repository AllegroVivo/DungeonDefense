from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("KingSlime",)

################################################################################
class KingSlime(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-127",
            name="King Slime",
            life=130,
            attack=14,
            defense=8,
            rank=3,
            dex=10,
            idle_frames=6
        )

################################################################################
