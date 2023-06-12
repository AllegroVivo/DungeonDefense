from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom           import DMBattleRoom
from utilities              import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("TheAbsolute",)

################################################################################
class TheAbsolute(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-136",
            name="The Absolute",
            description=(
                "Only one monster can be deployed in this room. The deployed "
                "monster's LIFE, ATK, DEF is increased by 200 (+60 per Lv) % "
                "and default DEX is increased by 200 %."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced,
            monster_cap=1
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        self.monsters[0].increase_stat_pct("life", self.effect_value() / 100)
        self.monsters[0].increase_stat_pct("attack", self.effect_value() / 100)
        self.monsters[0].increase_stat_pct("defense", self.effect_value() / 100)
        self.monsters[0].increase_stat_pct("dex", 2.0)

################################################################################
    def effect_value(self) -> int:

        return 200 + (60 * self.level)

################################################################################
