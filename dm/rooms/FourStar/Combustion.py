from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Combustion",)

################################################################################
class Combustion(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-154",
            name="Combustion",
            description=(
                "Inflicts {value} damage and deals additional damage as much "
                "as twice the Burn stat of the hero that entered the room."
            ),
            level=level,
            rank=4,
            base_dmg=49
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        damage = self.damage
        burn = unit.get_status("Burn")
        if burn is not None:
            damage += burn.stacks * 2

        unit.damage(damage)

################################################################################
