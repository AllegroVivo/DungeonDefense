from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Ignition",)

################################################################################
class Ignition(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-110",
            name="Ignition",
            description=(
                "Inflicts 1~18 (+0~17 per Lv) damage to hero that entered the "
                "room. Inflict additional damage as much as hero's Burn stat."
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
            burn = ctx.unit.get_status("Burn")
            if burn is not None:
                ctx.unit.damage(burn.stacks)

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 18)
        for _ in range(self.level):
            damage += random.randint(0, 17)

        return damage

################################################################################
