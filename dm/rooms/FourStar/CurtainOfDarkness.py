from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom
from utilities  import *

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("CurtainOfDarkness",)

################################################################################
class CurtainOfDarkness(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-124",
            name="Curtain of Darkness",
            description=(
                "Gives 1 (+1 per Lv) Blind to heroes that entered the room. "
                "Give 3 (+1 per Lv) Defense to all monsters in adjacent rooms "
                "at the beginning of the battle."
            ),
            level=level,
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)
        self.game.subscribe_event("before_battle", self.before_battle)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit += self.game.spawn("Blind", stacks=self.effect_value())

################################################################################
    def before_battle(self) -> None:

        adj_rooms = self.game.dungeon.get_adjacent_rooms(self.position)
        monsters = []
        for room in adj_rooms:
            try:
                monsters.extend(room.monsters)  # type: ignore
            except AttributeError:
                continue

        for monster in monsters:
            monster += self.game.spawn("Defense", stacks=self.defense_value())

################################################################################
    def effect_value(self) -> int:

        return 1 + (1 * self.level)

################################################################################
    def defense_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
