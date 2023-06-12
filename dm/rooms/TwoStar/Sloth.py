from __future__ import annotations

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Sloth",)

################################################################################
class Sloth(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-112",
            name="Sloth",
            description=(
                "Gives 3 (+1 per Lv) Weak and 3 (+1 per Lv) Slow to heroes "
                "that entered the room."
            ),
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
            ctx.unit += self.game.spawn("Weak", stacks=self.effect_value())
            ctx.unit += self.game.spawn("Slow", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
