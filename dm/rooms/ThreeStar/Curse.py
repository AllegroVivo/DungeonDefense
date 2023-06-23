from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurseRoom",)

################################################################################
class CurseRoom(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-136",
            name="Curse",
            description=(
                "Inflicts {damage} damage, give {status} Weak, and {status} "
                "Vulnerable to the hero that entered the room."
            ),
            level=level,
            rank=3,
            base_dmg=7,
            effects=[
                Effect(name="Weak", base=3, per_lv=3),
                Effect(name="Vulnerable", base=3, per_lv=3),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)
        unit.add_status("Weak", self.effects["Weak"], self)
        unit.add_status("Vulnerable", self.effects["Vulnerable"], self)

################################################################################
