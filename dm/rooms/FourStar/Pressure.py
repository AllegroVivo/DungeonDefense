from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Pressure",)

################################################################################
class Pressure(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-122",
            name="Pressure",
            description=(
                "DEX of heroes in the room is decreased by 10 (+1 per Lv) %. "
                "Gives 1 (+1 per Lv) Slow to heroes that entered the room."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit.mutate_stat("dex", -self.effect_value())
            ctx.unit += self.game.spawn("Slow", stacks=1 + (1 * self.level))

################################################################################
    def effect_value(self) -> int:

        return (10 + (50 * self.level)) // 100

################################################################################
