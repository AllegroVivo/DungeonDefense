from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("HealingWind",)

################################################################################
class HealingWind(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-126",
            name="Healing Wind",
            description=(
                "Applies 32 (+16 per Lv) Regeneration to all monsters in the "
                "dungeon when a hero enters the room."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.game.dungeon.deployed_monsters:
                monster += self.game.spawn("Regeneration", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 32 + (16 * self.level)

################################################################################
