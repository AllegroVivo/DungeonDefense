from __future__ import annotations

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Amplify",)

################################################################################
class Amplify(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-115",
            name="Amplify",
            description=(
                "Applies 3 (+3 per Lv) Vulnerable to heroes that entered the room."
            ),
            level=level,
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit += self.game.spawn("Vulnerable", stacks=3)

################################################################################
