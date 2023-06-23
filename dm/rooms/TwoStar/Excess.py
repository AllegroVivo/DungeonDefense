from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Excess",)

################################################################################
class Excess(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-112",
            name="Excess",
            description=(
                "Give {value} Slow to heroes in the room when a hero enters."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Slow", base=3, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for hero in self.heroes:
            hero.add_status("Slow", self.effects["Slow"], self)

################################################################################
