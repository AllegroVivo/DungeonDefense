from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("OrcGirl",)

################################################################################
class OrcGirl(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-117",
            name="Orc Girl",
            life=90,
            attack=16,
            defense=7,
            rank=3,
            dex=10
        )

################################################################################
