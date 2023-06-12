from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("HellHound",)

################################################################################
class HellHound(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-112",
            name="Hell Hound",
            life=80,
            attack=10,
            defense=4.0,
            rank=2,
            dex=10,
            idle_frames=4
        )

################################################################################
