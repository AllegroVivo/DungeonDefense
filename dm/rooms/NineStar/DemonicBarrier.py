from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from ..chargable        import DMChargeable
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("DemonicBarrier",)

################################################################################
class DemonicBarrier(DMBattleRoom, DMChargeable):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-139",
            name="Demonic Barrier",
            description=(
                "Once recharged, give 1 (+1 per Lv) Shield and 1 (+1 per Lv) "
                "Immune to all monsters in the dungeon. Monsters deployed in "
                "adjacent rooms will have their LIFE and DEF increased by "
                "40 (+10 per Lv) %."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:

        self.register_listener(self.game)
        self.game.subscribe_event("stat_calculation", self.stat_calculate)

################################################################################
    def activate(self) -> None:

        for monster in self.game.dungeon.deployed_monsters:
            monster += self.game.spawn("Shield", stacks=1 + (1 * self.level))
            monster += self.game.spawn("Immune", stacks=1 + (1 * self.level))

################################################################################
    def effect_value(self) -> int:

        return 40 + (10 * self.level)

################################################################################
    def stat_calculate(self) -> None:

        monsters = self.game.dungeon.get_adjacent_monsters(self.position, include_current=True)
        for monster in monsters:
            monster.increase_stat_pct("life", self.effect_value() / 100)
            monster.increase_stat_pct("defense", self.effect_value() / 100)

################################################################################
