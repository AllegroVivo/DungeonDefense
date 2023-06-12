from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Extraction",)

################################################################################
class Extraction(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-118",
            name="Extraction",
            description=(
                "Inflicts 1~3 (+0~2 per Lv) damage and collects 1 (+0.5 per Lv) "
                "information from hero that entered the room. When 100 pieces "
                "of information are collected, a random monster is upgraded."
            ),
            level=level,
            rank=3
        )

        self._total_data: float = 0.0

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit.damage(self.effect_value())
            self._total_data += self.collect_amount()

            if self._total_data >= 100.0:
                self.game.dungeon.upgrade_random_monster()
                self._total_data -= 100.0

################################################################################
    def effect_value(self) -> int:

        data = random.randint(1, 3)
        for _ in range(self.level):
            data += random.randint(0, 2)

        return data

################################################################################
    def collect_amount(self) -> float:

        return 1 + (0.5 * self.level)

################################################################################
