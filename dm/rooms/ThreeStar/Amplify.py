from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Amplify",)

################################################################################
class Amplify(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-135",
            name="Amplify",
            description=(
                "Gives {value} Vulnerable to heroes that entered the room."
            ),
            level=level,
            rank=3,
            effects=[
                Effect(name="Vulnerable", base=3, per_lv=3),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Vulnerable", self.effects["Vulnerable"], self)

################################################################################
