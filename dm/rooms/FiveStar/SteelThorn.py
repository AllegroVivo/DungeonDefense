from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom           import DMBattleRoom
from utilities              import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("SteelThorn",)

################################################################################
class SteelThorn(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-135",
            name="Steel Thorn",
            description=(
                "Gives 36 (+24 per Lv) Armor and 36 (+24 per Lv) Thorn to "
                "deployed monsters whenever a hero enters."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Armor", stacks=self.effect_value())
                monster += self.game.spawn("Thorn", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 36 + (24 * self.level)

################################################################################
