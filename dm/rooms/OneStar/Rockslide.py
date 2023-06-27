from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from ...core.objects.unit import DMUnit
################################################################################

__all__ = ("Rockslide",)


################################################################################
class Rockslide(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):
        super().__init__(
            game, position,
            _id="ROOM-109",
            name="Rockslide",
            description=(
                "Inflicts {damage} damage to the hero that entered the room. "
                "If the hero is under effect of Slow, triple the damage will "
                "be inflicted."
            ),
            level=level,
            rank=1
        )

    ################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        # Get base damage.
        damage = self.dmg
        # If the hero is under the effect of Slow, triple the damage.
        slow = unit.get_status("Slow")
        if slow is not None:
            damage *= 3.0  # Triple the damage.
        # Apply.
        unit.damage(damage)

################################################################################
