from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.rooms.battleroom import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("Sacrifice",)

################################################################################
class Sacrifice(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-116",
            name="Sacrifice",
            description=(
                "Dark Lord's LIFE is restored by 2 (+1 per Lv) % if enemy "
                "dies in the room."
            ),
            level=level,
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")
        if ctx.room == self:
            self.game.dark_lord.heal((0.02 * (1 * self.level)) * self.game.dark_lord.max_life)

################################################################################
    def effect_value(self) -> int:

        return 6 + (6 * self.level)

################################################################################
