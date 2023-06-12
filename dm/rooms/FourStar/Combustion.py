from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom
from utilities  import *

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Combustion",)

################################################################################
class Combustion(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-123",
            name="Combustion",
            description=(
                "Inflicts 1~49 (+0~48 per Lv) damage and deals additional "
                "damage as much as twice the Burn stat owned by the hero that "
                "entered the room."
            ),
            level=level,
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            damage = self.effect_value()
            burn = ctx.unit.get_status("Burn")
            if burn is not None:
                damage += (burn.stacks * 2)
            ctx.unit.damage(damage)

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 49)
        for _ in range(self.level):
            damage += random.randint(0, 48)

        return damage

################################################################################
