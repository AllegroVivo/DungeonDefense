from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("BloodPool",)

################################################################################
class BloodPool(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-124",
            name="Blood Pool",
            description=(
                "Give 20 (+12 per Lv) Vampire and Fury to all monsters in "
                "this and adjacent rooms whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

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
                monster += self.game.spawn("Vampire", stacsk=self.effect_value())
                monster += self.game.spawn("Fury", stacks=self.effect_value())

################################################################################
    def effect_value(self) -> int:

        return 20 + (12 * self.level)

################################################################################
