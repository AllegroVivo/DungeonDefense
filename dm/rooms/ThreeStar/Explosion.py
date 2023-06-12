from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Explosion",)

################################################################################
class Explosion(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-117",
            name="Explosion",
            description=(
                "Inflicts 1~6 (+0~6 per Lv) damage to all enemies in the current "
                "room and all adjacent rooms when a hero enters the room."
            ),
            level=level,
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            adj_rooms = self.game.dungeon.get_adjacent_rooms(self.position, include_current=True)
            heroes = []
            for room in adj_rooms:
                heroes.extend(room.heroes)

            for hero in heroes:
                hero.damage(self.effect_value())

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 6)
        for _ in range(self.level):
            damage += random.randint(0, 6)

        return damage

################################################################################
