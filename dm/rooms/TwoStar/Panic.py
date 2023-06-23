from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PanicRoom",)

################################################################################
class PanicRoom(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-122",
            name="Panic",
            description=(
                "Gives {value} Panic to heroes that enter the room."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Panic", base=1, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Panic", self.effects["Panic"], self)

################################################################################
