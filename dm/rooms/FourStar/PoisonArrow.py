from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PoisonArrow",)

################################################################################
class PoisonArrow(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-161",
            name="Poison Arrow",
            description=(
                "Inflicts {damage} damage and give {status} Poison to hero "
                "that entered the room."
            ),
            level=level,
            rank=4,
            base_dmg=27,
            effects=[
                Effect(name="Poison", base=16, per_lv=8),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.dmg)
        unit.add_status("Poison", self.effects["Poison"], self)

################################################################################
