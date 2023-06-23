from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sloth",)

################################################################################
class Sloth(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-127",
            name="Sloth",
            description=(
                "Gives {value} Weak and {value} Slow to all heroes that enter "
                "the room."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Weak", base=3, per_lv=1),
                Effect(name="Slow", base=3, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Weak", self.effects["Weak"], self)
        unit.add_status("Slow", self.effects["Slow"], self)

################################################################################
