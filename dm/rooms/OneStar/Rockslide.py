from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Rockslide",)

################################################################################
class Rockslide(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-104",
            name="Rockslide",
            description=(
                "Inflicts 1~16 (+0~15 per Lv) damage to the hero that entered "
                "the room. If the hero is under effect of Slow, damage is tripled."
            ),
            level=level,
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            scalar = 1.0  # 100 % effectiveness
            slow = ctx.unit.get_status("Slow")
            if slow is not None:
                scalar = 3.0  # 300 % effectiveness
            ctx.unit.damage(self.effect_value() * scalar)

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 16)
        for _ in range(self.level):
            damage += random.randint(0, 15)

        return damage

################################################################################
