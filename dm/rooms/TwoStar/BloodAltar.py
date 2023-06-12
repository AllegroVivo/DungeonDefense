from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("BloodAltar",)

################################################################################
class BloodAltar(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-105",
            name="Blood Altar",
            description=(
                "Gives 20 (+12 per Lv) Vampire to deployed monsters whenever "
                "a hero enters the room."
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
                monster += self.game.spawn("Vampire", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 20 + (12 * self.level)

################################################################################
