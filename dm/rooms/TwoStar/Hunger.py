from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Hunger",)

################################################################################
class Hunger(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-124",
            name="Hunger",
            description=(
                "Reduces ATK of the heroes that entered the room by {value}."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="ATK", base=3, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.reduce_stat_flat("atk", self.effects["ATK"])

################################################################################
