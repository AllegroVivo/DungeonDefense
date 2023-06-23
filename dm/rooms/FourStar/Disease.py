from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Disease",)

################################################################################
class Disease(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-167",
            name="Disease",
            description=(
                "Gives {value} Poison and Corpse Explosion to heroes that "
                "entered the room."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Poison", base=24, per_lv=16),
                Effect(name="Corpse Explosion", base=24, per_lv=16),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Poison", self.effects["Poison"], self)
        unit.add_status("Corpse Explosion", self.effects["Corpse Explosion"], self)

################################################################################
