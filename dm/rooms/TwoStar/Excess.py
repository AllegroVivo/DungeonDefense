from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Excess",)

################################################################################
class Excess(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-106",
            name="Excess",
            description=(
                "Give 3 (+1 per Lv) Slow to heroes in the room when a hero "
                "enters a room."
            ),
            level=level,
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit += self.game.spawn("Slow", stacks=self.effect_value())
            for hero in ctx._target.heroes:
                hero += self.game.spawn("Slow", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
