from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("CurseRoom",)

################################################################################
class CurseRoom(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-116",
            name="Curse",
            description=(
                "Inflicts 1~7 (+0~6 per Lv) damage, give 2 (+1 per Lv) Weak, "
                "and 2 (+1 per Lv) Vulnerable to the hero that entered the room."
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
            ctx.unit.damage(self.effect_value())
            ctx.unit += self.game.spawn("Weak", stacks=self.debuff_value())
            ctx.unit += self.game.spawn("Vulnerable", stacks=self.debuff_value())

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 7)
        for _ in range(self.level):
            damage += random.randint(0, 6)

        return damage

################################################################################
    def debuff_value(self) -> int:

        return 2 + (1 * self.level)

################################################################################
