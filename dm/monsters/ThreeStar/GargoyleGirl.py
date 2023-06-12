from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("GargoyleGirl",)

################################################################################
class GargoyleGirl(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):
        super().__init__(
            game,
            level,
            _id="MON-126",
            name="Gargoyle Girl",
            life=130,
            attack=14,
            defense=7,
            rank=3,
            dex=10,
            idle_frames=6
        )

################################################################################
