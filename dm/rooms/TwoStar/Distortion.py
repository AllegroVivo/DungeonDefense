from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Distortion",)

################################################################################
class Distortion(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-121",
            name="Distortion",
            description=(
                "Gives {value} Haze to heroes that enter the room."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="Haze", base=1, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Haze", self.effects["Haze"], self)

################################################################################
