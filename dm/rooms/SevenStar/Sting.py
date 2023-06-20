from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from dm.rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Sting",)

################################################################################
class Sting(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-213",
            name="Sting",
            description=(
                "Once recharged, give {value} Poison to a random enemy in "
                "the adjacent area."
            ),
            level=level,
            rank=7,
            unlock=UnlockPack.Myth
        )

        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        target = random.choice(targets)
        target.add_status("Poison", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **status = b + (a * LV)**

        In this functions:

        - b is the base status.
        - a is the additional stacks per level.
        - LV is the level of this room.
        """

        return 64 + (56 * self.level)

################################################################################
