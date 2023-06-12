from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from ..chargable    import DMChargeable
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame
################################################################################

__all__ = ("SwirlOfAnger",)

################################################################################
class SwirlOfAnger(DMBattleRoom, DMChargeable):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-137",
            name="Swirl of Anger",
            description=(
                "Once recharged, give 200 (+200 per Lv) Fury and 1 Merciless "
                "to all monsters in adjacent area."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:

        self.register_listener(self.game)

################################################################################
    def activate(self) -> None:

        monsters = self.game.dungeon.get_adjacent_monsters(self.position, include_current=True)
        for monster in monsters:
            monster += self.game.spawn("Fury", stacks=self.effect_value())
            monster += self.game.spawn("Merciless")

################################################################################
    def effect_value(self) -> int:

        return 200 + (200 * self.level)

################################################################################
