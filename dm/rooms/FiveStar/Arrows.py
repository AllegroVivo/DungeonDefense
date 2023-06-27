from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Arrows",)

################################################################################
class Arrows(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-181",
            name="Arrows",
            description=(
                "Inflicts {value} damage to all enemies in this room when a "
                "hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original,
            base_dmg=34
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for hero in self.heroes:
            hero.damage(self.dmg)

################################################################################
