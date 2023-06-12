from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Gargoyle",)

################################################################################
class Gargoyle(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):

        super().__init__(
            game,
            level,
            _id="MON-113",
            name="Gargoyle",
            life=90,
            attack=9,
            defense=5.5,
            rank=2,
            dex=10
        )

################################################################################
