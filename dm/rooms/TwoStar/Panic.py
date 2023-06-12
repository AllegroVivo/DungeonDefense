from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("PanicRoom",)

################################################################################
class PanicRoom(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-107",
            name="Panic",
            description="Gives 1 (+1 per Lv) Panic to heroes that enter the room.",
            level=level,
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit += self.game.spawn("Panic", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 1 + (1 * self.level)

################################################################################
