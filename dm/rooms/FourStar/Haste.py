from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("DoubleGiant",)

################################################################################
class DoubleGiant(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-119",
            name="Haste",
            description=(
                "DEX of deployed monster is increased by 10 (+1 per Lv) %. "
                "Gives 2 (+1 per Lv) Acceleration to deployed monsters whenever "
                "a hero enters the room."
            ),
            level=level,
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify_stat_calc)
        self.game.subscribe_event("on_room_change", self.notify_room_change)

################################################################################
    def notify_stat_calc(self, **kwargs) -> None:

        for monster in self.monsters:
            monster.mutate_stat("dex", 0.10 + (0.01 * self.level))

################################################################################
    def notify_room_change(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Acceleration", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 2 + (1 * self.level)

################################################################################
