from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Sprout",)

################################################################################
class Sprout(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-111",
            name="Sprout",
            description=(
                "Gives 32 (+16 per Lv.) Regeneration to deployed monsters "
                "whenever a hero enters."
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
                monster += self.game.spawn("Acceleration", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 3 + (1 * self.level)

################################################################################
