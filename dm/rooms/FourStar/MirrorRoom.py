from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("MirrorRoom",)

################################################################################
class MirrorRoom(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-130",
            name="Mirror Room",
            description=(
                "Gives 1 (+1 per Lv) Mirror and 20 (+20 per Lv) Pleasure to "
                "deployed monsters whenever a hero enters."
            ),
            level=level,
            rank=4,
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
                monster += self.game.spawn("Mirror", stacks=1 + (1 * self.level))
                monster += self.game.spawn("Pleasure", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 20 + (20 * self.level)

################################################################################
