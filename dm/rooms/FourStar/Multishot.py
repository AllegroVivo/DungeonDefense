from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Multishot",)

################################################################################
class Multishot(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-160",
            name="Multishot",
            description=(
                "Inflicts {value} damage to 3 enemies in this room when a "
                "hero enters the room."
            ),
            level=level,
            rank=4,
            base_dmg=34
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        options = self.units_of_type(unit)
        targets = self.random.sample(options, 3)
        for target in targets:
            target.damage(self.damage)

################################################################################
