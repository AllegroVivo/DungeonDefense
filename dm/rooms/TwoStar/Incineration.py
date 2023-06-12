from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Incineration",)

################################################################################
class Incineration(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-111",
            name="Incineration",
            description=(
                "Inflicts 1~21 (+0~20 per Lv) damage and give 32 (+16 per Lv) "
                "Burn to hero that entered the room."
            ),
            level=level,
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            ctx.unit.damage(self.effect_value())
            ctx.unit += self.game.spawn("Burn", stacks=self.burn_value())

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 21)
        for _ in range(self.level):
            damage += random.randint(0, 20)

        return damage

################################################################################
    def burn_value(self) -> int:

        return 32 + (16 * self.level)

################################################################################
