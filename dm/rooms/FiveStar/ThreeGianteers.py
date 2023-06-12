from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("ThreeGianteers",)

################################################################################
class ThreeGianteers(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-121",
            name="Three Gianteers",
            description=(
                "Deployed monsters will gigantify and get 2(+1 per Lv)x LIFE "
                "and 2(+1 pr Lv)x ATK."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        for monster in self.monsters:
            monster.mutate_stat("life", float(self.effect_value()))
            monster.mutate_stat("attack", float(self.effect_value()))

################################################################################
    def effect_value(self) -> int:

        return 2 + (1 * self.level)

################################################################################
