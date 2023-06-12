from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("BiggerFight",)

################################################################################
class BiggerFight(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-128",
            name="Bigger Fight",
            description=(
                "Increases the number of deployable monsters by 2. The deployed "
                "monsters' ATK and LIFE is increased by 50 (+25 per Lv) %. Gives "
                "1 Rampage to deployed monsters whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening,
            monster_cap=5
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("stat_calculation", self.stat_calc)
        self.game.subscribe_event("on_room_change", self.room_change)

################################################################################
    def stat_calc(self) -> None:

        for monster in self.monsters:
            monster.increase_stat_pct("life", self.effect_value() / 100)
            monster.increase_stat_pct("attack", self.effect_value() / 100)

################################################################################
    def room_change(self, **kwargs):

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Rampage")

################################################################################
    def effect_value(self) -> int:

        return 50 + (25 * self.level)

################################################################################
