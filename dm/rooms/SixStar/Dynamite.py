from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("Dynamite",)

################################################################################
class Dynamite(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-123",
            name="Dynamite",
            description=(
                "When a hero in this room dies, inflict 300 (+50 per Lv) % of "
                "the dead hero's Burn stat to all heroes in adjacent rooms."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")
        if ctx.room == self:
            burn = ctx.defender.get_status("Burn")
            if burn is not None:
                adj_rooms = self.game.dungeon.get_adjacent_rooms(self.position, include_current=True)
                heroes = []
                for room in adj_rooms:
                    heroes.extend(room.heroes)
                for hero in heroes:
                    hero.damage(burn.stacks * self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return (300 + (50 * self.level)) // 100

################################################################################
