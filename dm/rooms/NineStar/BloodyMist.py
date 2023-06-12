from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from ..chargable        import DMChargeable
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("BloodyMist",)

################################################################################
class BloodyMist(DMBattleRoom, DMChargeable):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-140",
            name="Bloody Mist",
            description=(
                "Once recharged, give 96 (+72 per Lv) Vampire and 96 (+72 per Lv) "
                "Fury to all monsters in the dungeon. When monsters in adjacent rooms "
                "receive damage, get Vampire as much as 20 (+1 per Lv) % of ATK."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:

        self.register_listener(self.game)
        self.game.subscribe_event("on_attack", self.on_attack)

################################################################################
    def activate(self) -> None:

        for monster in self.game.dungeon.deployed_monsters:
            monster += self.game.spawn("Vampire", stacks=self.effect_value())
            monster += self.game.spawn("Fury", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 96 + (72 * self.level)

################################################################################
    def on_attack(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")

        monsters = self.game.dungeon.get_adjacent_monsters(self.position)
        if ctx.defender in monsters:
            for monster in self.monsters:
                monster += self.game.spawn("Vampire", stacks=20 + (1 * self.level))

################################################################################
