from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("InfinityClock",)

################################################################################
class InfinityClock(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-142",
            name="Infinity Clock",
            description=(
                "Boost DEX of monsters in adjacent rooms by 100 (+4 per Lv) %, "
                "and when hero enters, give 5 (+1 per Lv) Acceleration to "
                "monsters in adjacent rooms."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculate", self.stat_calculate)

################################################################################
    def stat_calculate(self) -> None:

        monsters = self.game.dungeon.get_adjacent_monsters(self.position, include_current=True)
        for monster in monsters:
            monster.increase_stat_pct("dex", 1.0 + (0.04 * self.level))

################################################################################
    def on_enter(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            monsters = self.game.dungeon.get_adjacent_monsters(self.position, include_current=True)
            for monster in monsters:
                monster += self.game.spawn("Acceleration", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 5 + (1 * self.level)

################################################################################
