from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Blitz",)

################################################################################
class Blitz(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-105",
            name="Blitz",
            description=(
                "Inflicts {value} damage to hero that entered the room. If hero "
                "is under the effect of Haze or Charm, 3x damage is inflicted."
            ),
            level=level,
            rank=1,
            unlock=UnlockPack.Original,
            base_dmg=15
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        # Establish the base damage.
        damage = self.damage

        # If the hero is under the effect of Haze or Charm, triple that.
        haze = unit.get_status("Haze")
        charm = unit.get_status("Charm")
        if haze or charm:
            damage *= 3

        # Then apply.
        unit.damage(damage)

################################################################################
