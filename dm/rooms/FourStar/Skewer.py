from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Skewer",)

################################################################################
class Skewer(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-163",
            name="Skewer",
            description=(
                "Inflicts {value} damage and temporarily immobilize all enemies "
                "in the room when a hero enters the room."
            ),
            level=level,
            rank=4,
            base_dmg=37
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.dmg)
        for hero in self.heroes:
            hero.immobilize(1.5)  # Extra .5 seconds seems fair for an upgraded room.

################################################################################
