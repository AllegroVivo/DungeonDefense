from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom
from utilities  import *

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Blitz",)

################################################################################
class Blitz(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-121",
            name="Blitz",
            description=(
                "Inflicts 1~14 (+0~14 per Lv) damage to hero that entered the "
                "room. If hero is under the effect of Haze or Charm, 3x damage "
                "is inflicted."
            ),
            level=level,
            rank=1,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_enter", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            haze = ctx.unit.get_status("Haze")
            charm = ctx.unit.get_status("Charm")
            damage = self.effect_value()
            if haze or charm:
                damage *= 3
            ctx.unit.damage(damage)

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 14)
        for _ in range(self.level):
            damage += random.randint(0, 14)

        return damage

################################################################################
