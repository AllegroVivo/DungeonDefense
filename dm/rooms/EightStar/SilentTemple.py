from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from ..chargable        import DMChargeable
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("SilentTemple",)

################################################################################
class SilentTemple(DMBattleRoom, DMChargeable):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-138",
            name="Silent Temple",
            description=(
                "Once recharged, give 10 (+2 per Lv) Focus to all monsters in "
                "the dungeon. Monsters in adjacent area will inflict 5 % extra "
                "damage per Focus stack."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:

        self.register_listener(self.game)
        self.game.subscribe_event("on_attack", self.on_attack)

################################################################################
    def activate(self) -> None:

        for monster in self.game.dungeon.deployed_monsters:
            monster += self.game.spawn("Fury", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 10 + (2 * self.level)

################################################################################
    def on_attack(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")
        monsters = self.game.dungeon.get_adjacent_monsters(self.position, include_current=True)
        for monster in monsters:
            focus = monster.get_status("Focus")
            if focus is not None:
                focus.amplify_pct(0.05)

################################################################################
