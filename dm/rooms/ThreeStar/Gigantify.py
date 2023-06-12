from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.rooms.battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core import DMGame
################################################################################

__all__ = ("Gigantify",)

################################################################################
class Gigantify(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-113",
            name="Gigantify",
            description=(
                "You can only deploy 1 monster in this room, but the monster "
                "will gigantify and get 2(+1 per 2Lv)x LIFE and 2(+1 per 2Lv)x "
                "ATK."
            ),
            level=level,
            rank=3,
            monster_cap=1
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        for monster in self.monsters:
            monster.mutate_stat("attack", self.effect_value())
            monster.mutate_stat("life", self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 2 + (1 * self.level // 2)

################################################################################
