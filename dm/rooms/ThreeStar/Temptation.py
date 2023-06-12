from __future__ import annotations

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom
from utilities  import *

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Temptation",)

################################################################################
class Temptation(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-120",
            name="Temptation",
            description="Give 1 (+1 per Lv) Charm to hero that entered the room.",
            level=level,
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit += self.game.spawn("Charm", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 1 + (1 * self.level)

################################################################################
