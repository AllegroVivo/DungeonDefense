from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("BiggerRoom",)

################################################################################
class BiggerRoom(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-127",
            name="Bigger Room",
            description=(
                "Increases the number of deployable monsters by 1. The deployed "
                "monsters' LIFE is increased by 50 (+25 per Lv) %."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening,
            monster_cap=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        for monster in self.monsters:
            monster.increase_stat_pct("life", self.effect_value() / 100)

################################################################################
    def effect_value(self) -> int:

        return 50 + (25 * self.level)

################################################################################
