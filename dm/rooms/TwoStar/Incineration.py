from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Incineration",)

################################################################################
class Incineration(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-126",
            name="Incineration",
            description=(
                "Inflicts {damage} damage and give {status} Burn to the hero "
                "that entered the room."
            ),
            level=level,
            rank=2,
            base_dmg=21,
            effects=[
                Effect(name="Burn", base=32, per_lv=16),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)
        unit.add_status("Burn", self.effects["Burn"], self)

################################################################################
