from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom
from utilities  import *

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Warhorn",)

################################################################################
class Warhorn(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-126",
            name="Warhorn",
            description=(
                "Gives 16 (+8 per Lv) Fury to all monsters in the dungeon "
                "when a hero enters."
            ),
            level=level,
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.game.dungeon.deployed_monsters:
                monster += self.game.spawn("Fury", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 16 + (8 * self.level)

################################################################################
