from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("SwordAndShield",)

################################################################################
class SwordAndShield(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-112",
            name="Sword and Shield",
            description=(
                "ATK and DEF of the deployed monsters are increased by 5 (+5 per Lv)."
            ),
            level=level,
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        for monster in self.monsters:
            monster.mutate_stat("attack", self.effect_value())
            monster.mutate_stat("defense", self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 5 + (5 * self.level)

################################################################################
