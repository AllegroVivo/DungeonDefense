from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from ...core    import DMFighter, DMGame, RoomChangeContext
################################################################################

__all__ = ("Guillotine",)

################################################################################
class Guillotine(DMTrapRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="TRP-108",
            name="Guillotine",
            description=(
                "Inflicts 1~24 (+0~23 per Lv) damage to the hero that entered "
                "the room. The lower the LIFE of the hero is, the more damage "
                "is inflicted."
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
            ctx.unit.damage(self.scaled_effect(ctx.unit))

################################################################################
    def effect_value(self) -> int:

        damage = random.randint(1, 24)
        for _ in range(self.level):
            damage += random.randint(0, 23)

        return damage

################################################################################
    def scaled_effect(self, unit: DMFighter) -> int:

        health_ratio = unit.life / unit.max_life
        scalar = 1 + 2 * (1 - health_ratio)

        return int(self.effect_value() * scalar)

################################################################################
