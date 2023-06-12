from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("TreeOfLife",)

################################################################################
class TreeOfLife(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-125",
            name="Tree of Life",
            description=(
                "Gives 32 (+16 per Lv) Regeneration to all monsters in adjacent "
                "rooms whenever a hero enters the room. Gives 1 Absorption to "
                "all monsters in adjacent rooms at the beginning of the battle."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening
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
            monster += self.game.spawn("Absorption")

################################################################################
    def on_room_change(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            adj_rooms = self.game.dungeon.get_adjacent_rooms(self.position, include_current=True)
            monsters = []
            for room in adj_rooms:
                try:
                    monsters.extend(room.monsters)  # type: ignore
                except AttributeError:
                    pass
            for monster in monsters:
                monster += self.game.spawn("Regeneration", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 32 + (16 * self.level)

################################################################################
