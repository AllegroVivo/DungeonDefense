from __future__ import annotations

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Hunger",)

################################################################################
class Hunger(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-109",
            name="Hunger",
            description=(
                "Reduces ATK of the heroes that entered the room by 3(+1 per Lv)."
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
            ctx.unit.reduce_stat_flat("attack", self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
