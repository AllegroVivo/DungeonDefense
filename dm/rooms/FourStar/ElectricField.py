from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom
from utilities  import *

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("ElectricField",)

################################################################################
class ElectricField(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-125",
            name="Electric Field",
            description=(
                "Gives 32 (+24 per Lv) Shock to all heroes in adjacent rooms "
                "when a hero enters the room."
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
            adj_rooms = self.game.dungeon.get_adjacent_rooms(self.position)
            heroes = []
            for room in adj_rooms:
                heroes.extend(room.heroes)
            for hero in heroes:
                hero += self.game.spawn("Shock", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 32 + (24 * self.level)

################################################################################
