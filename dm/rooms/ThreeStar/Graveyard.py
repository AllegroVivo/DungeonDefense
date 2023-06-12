from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.rooms.battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core import DMGame
################################################################################

__all__ = ("Graveyard",)

################################################################################
class Graveyard(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-114",
            name="Graveyard",
            description=(
                "Gives 2 (+1 per Lv) Immortality to all monsters in the room "
                "at the beginning of the battle."
            ),
            level=level,
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("before_battle", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        for monster in self.monsters:
            monster += self.game.spawn("Immortality", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 2 + (1 * self.level)

################################################################################
