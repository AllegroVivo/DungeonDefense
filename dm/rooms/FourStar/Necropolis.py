from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom       import DMBattleRoom
from ...core.objects    import DMMonster
from utilities          import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("Necropolis",)

################################################################################
class Necropolis(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-129",
            name="Necropolis",
            description=(
                "Gives 4 (+2 per Lv) Immortality to all monsters in the room at "
                "the beginning of the battle. When a deployed monster dies, give "
                "3 (+1 at Lv6,Lv16,Lv26,etc.) Immortality to all monsters."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening,
            monster_cap=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("before_battle", self.before_battle)
        self.game.subscribe_event("on_death", self.on_death)

################################################################################
    def before_battle(self) -> None:

        for monster in self.monsters:
            monster += self.game.spawn("Immortality", stacks=4 + (2 * self.level))

################################################################################
    def on_death(self, **kwargs):

        ctx: AttackContext = kwargs.get("ctx")
        if ctx.room == self:
            if isinstance(ctx.defender, DMMonster):
                for monster in self.game.dungeon.deployed_monsters:
                    monster += self.game.spawn("Immortality", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return int(3 + (1 * self.level * 0.25))

################################################################################
