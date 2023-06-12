from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Thunder",)

################################################################################
class Thunder(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-119",
            name="Thunder",
            description=(
                "Inflicts 1~18 (+0~17 per Lv) and applies 16 (+8 per Lv) Shock "
                "to a random hero in the dungeon when a hero enters the room."
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
            # Damage
            ctx.unit.damage(self.effect_value())

            # Random hero gets debuff
            random_hero = random.choice(self.game.dungeon.heroes)
            random_hero += self.game.spawn("Shock", stacks=self.shock_value())

################################################################################
    def effect_value(self) -> int:

        data = random.randint(1, 18)
        for _ in range(self.level):
            data += random.randint(0, 17)

        return data

################################################################################
    def shock_value(self) -> int:

        return 16 + (8 * self.level)

################################################################################
