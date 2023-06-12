from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Frenzy",)

################################################################################
class Frenzy(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-106",
            name="Frenzy",
            description=(
                "Gives 16 (+12 per Lv) Fury to deployed monsters whenever a "
                "hero enters."
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
            for monster in self.monsters:
                monster += self.game.spawn("Fury", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 16 + (12 * self.level)

################################################################################
