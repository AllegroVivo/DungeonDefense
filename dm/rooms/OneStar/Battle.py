from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("Battle",)

################################################################################
class Battle(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position or Vector2(-1, -1),
            _id="BTL-101",
            name="Battle",
            description=(
                "Deployed monsters' maximum LIFE is increased by [y]25(+5 per Lv)."
            ),
            level=level,
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        for monster in self.monsters:
            monster.mutate_stat("life", self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 25 + (5 * self.level)

################################################################################
