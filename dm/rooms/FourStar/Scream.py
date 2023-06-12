from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("Scream",)

################################################################################
class Scream(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-120",
            name="Scream",
            description=(
                "Gives 1 (+1 per Lv) Panic to all enemies in the dungeon when "
                "a hero dies in this room."
            ),
            level=level,
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")
        if ctx.room == self:
            for hero in self.game.dungeon.heroes:
                hero += self.game.spawn("Panic", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 1 + (1 * self.level)

################################################################################
