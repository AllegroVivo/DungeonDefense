from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Return",)

################################################################################
class Return(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-128",
            name="Return",
            description=(
                "The 3rd enemy is returned to the dungeon entrance. The number "
                "of entries required for operation increases with each "
                "activation. It works up to {value} times."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="returns", base=3, per_lv=1),
            ]
        )

        self._count: int = 0
        self._triggers: int = 0

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        # If we've triggered this room the max number of times, do nothing.
        if self._triggers > self.effects["returns"]:
            return

        # Increment the count and check if the hero is the third hero
        # to enter this room.
        self._count += 1
        # If we've hit the third hero to enter.
        if self._count == 3:
            # Return the hero to the dungeon entrance.
            unit.room = self.game.dungeon.entrance
            # Increment the number of times this room has been triggered.
            self._triggers += 1
            # And reset the entry count.
            self._count = 0

################################################################################
