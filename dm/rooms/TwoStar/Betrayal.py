from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Betrayal",)

################################################################################
class Betrayal(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-115",
            name="Betrayal",
            description=(
                "Gives 6 (+6 per Lv) Pleasure to monsters in the room whenever "
                "a hero enters."
            ),
            level=level,
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Pleasure", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 6 + (6 * self.level)

################################################################################
