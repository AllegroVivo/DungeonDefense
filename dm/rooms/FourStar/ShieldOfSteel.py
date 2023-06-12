from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.rooms.battleroom import DMBattleRoom
from utilities              import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("ShieldOfSteel",)

################################################################################
class ShieldOfSteel(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-132",
            name="Shield of Steel",
            description=(
                "Gives 36 (+24 per Lv) Armor to deployed monsters whenever a "
                "hero enters. Gives 3 Shield to all monsters in adjacent rooms "
                "at the beginning of battle."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("before_battle", self.before_battle)
        self.game.subscribe_event("on_room_change", self.on_room_change)

################################################################################
    def before_battle(self) -> None:

        adj_rooms = self.game.dungeon.get_adjacent_rooms(self.position, include_current=True)

        monsters = []
        for room in adj_rooms:
            try:
                monsters.extend(room.monsters)  # type: ignore
            except AttributeError:
                pass

        for monster in monsters:
            monster += self.game.spawn("Shield", stacks=3)

################################################################################
    def on_room_change(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Armor", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 36 + (24 * self.level)

################################################################################
