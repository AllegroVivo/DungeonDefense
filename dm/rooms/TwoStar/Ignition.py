from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Ignition",)

################################################################################
class Ignition(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-125",
            name="Ignition",
            description=(
                "Inflicts {value} damage to hero that entered the room. Inflict "
                "additional damage as much the hero's Burn stat."
            ),
            level=level,
            rank=2,
            base_dmg=18
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        damage = self.damage

        burn = unit.get_status("Burn")
        if burn is not None:
            damage += burn.stacks

        unit.damage(damage)

################################################################################
