from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("Arrow",)

################################################################################
class Arrow(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-101",
            name="Arrow",
            description=(
                "Inflicts 1~18 (+0~17 per Lv) damage to the hero that entered "
                "the room."
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
            ctx.unit.damage(self.effect_value())

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 18)
        for _ in range(self.level):
            damage += random.randint(0, 17)

        return damage

################################################################################