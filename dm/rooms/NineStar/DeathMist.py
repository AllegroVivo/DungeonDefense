from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from ..chargable        import DMChargeable
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, DMStatus
################################################################################

__all__ = ("DeathMist",)

################################################################################
class DeathMist(DMBattleRoom, DMChargeable):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-141",
            name="Death Mist",
            description=(
                "Once recharged, give 3 (+1 per Lv) Immortality and 1 Immortal "
                "Rage to all monsters in adjacent area. Every time Immortality "
                "is triggered, monsters deployed in adjacent rooms will get Fury "
                "as much as 100 (+5 per Lv) % of ATK."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:

        self.register_listener(self.game)
        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def activate(self) -> None:

        for monster in self.game.dungeon.deployed_monsters:
            monster += self.game.spawn("Immortality", stacks=3 + (1 * self.level))
            monster += self.game.spawn("Immortal Rage")

################################################################################
    def effect_value(self) -> int:

        return 100 + (5 * self.level) // 100

################################################################################
    def notify(self, **kwargs) -> None:

        status: DMStatus = kwargs.get("status")
        if status.name == "Immortality":
            monsters = self.game.dungeon.get_adjacent_monsters(self.position, include_current=True)
            for monster in monsters:
                monster += self.game.spawn("Fury", stacks=self.effect_value() * monster.attack)

################################################################################
