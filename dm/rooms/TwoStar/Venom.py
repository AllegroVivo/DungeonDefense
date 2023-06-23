from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Venom",)

################################################################################
class Venom(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-129",
            name="Venom",
            description=(
                "Applies {value} Poison to heroes that entered the room."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Poison", base=20, per_lv=10),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Poison", self.effects["Poison"], self)

################################################################################
