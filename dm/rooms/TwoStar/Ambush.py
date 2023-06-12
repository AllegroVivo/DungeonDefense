from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from ...core    import DMGame
################################################################################

__all__ = ("Ambush",)

################################################################################
class Ambush(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-104",
            name="Ambush",
            description=(
                "ATK of monsters deployed in this room increases by 4 (+4 per Lv.) "
                "per trap in the dungeon."
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

################################################################################
    def effect_value(self) -> int:

        return (4 + (4 * self.level)) * len(self.game.dungeon.trap_rooms)

################################################################################
