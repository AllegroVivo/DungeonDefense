from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.unit import DMUnit

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Pit",)

################################################################################
class Pit(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-108",
            name="Pit",
            description=(
                "Inflicts {damage} damage and temporarily immobilizes each "
                "hero that enters the room."
            ),
            level=level,
            rank=1,
            base_dmg=16
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)
        unit.immobilize(1.0)  # 1 second seems good?

################################################################################
