from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("Cerberus",)

################################################################################
class Cerberus(DMMonster):

    def __init__(self, game: DMGame, level: int = 1):
        super().__init__(
            game,
            level,
            _id="MON-131",
            name="Cerberus",
            life=130,
            attack=14,
            defense=5.5,
            rank=3,
        )

################################################################################
