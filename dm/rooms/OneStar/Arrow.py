from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Arrow",)

################################################################################
class Arrow(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-104",
            name="Arrow",
            description=(
                "Inflicts {damage} damage to each hero that enters the room."
            ),
            level=level,
            rank=1,
            base_dmg=18
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.dmg)

################################################################################
