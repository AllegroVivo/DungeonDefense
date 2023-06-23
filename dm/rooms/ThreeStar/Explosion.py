from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Explosion",)

################################################################################
class Explosion(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-137",
            name="Explosion",
            description=(
                "Inflicts {value} damage to all enemies in the current room "
                "and all adjacent rooms when a hero enters the room."
            ),
            level=level,
            rank=3,
            base_dmg=6
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        targets = []
        # compile a list of targets in those rooms
        for room in self.adjacent_rooms + [self]:
            targets.extend(room.get_heroes_or_monsters(unit))

        # Deal damage to all targets in the affected rooms
        for target in targets:
            target.damage(self.damage)

################################################################################
