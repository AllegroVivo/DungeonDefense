from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Lightning",)

################################################################################
class Lightning(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-159",
            name="Lightning",
            description=(
                "Inflicts {damage} damage and give {status} Shock to hero "
                "that entered the room."
            ),
            level=level,
            rank=4,
            base_dmg=34,
            effects=[
                Effect(name="Shock", base=32, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)
        unit.add_status("Shock", self.effects["Shock"], self)

################################################################################
