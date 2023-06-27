from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import StatusApplicationContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("RainbowFlower",)

################################################################################
class RainbowFlower(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-209",
            name="Rainbow Flower",
            description=(
                "Burn, Shock, Poison, Corpse Explosion given by adjacent traps "
                "will increase by {value} %."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="buff", base=25, per_lv=5),
            ]
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if ctx.source in self.adjacent_rooms + [self]:
            if ctx.status.name in ("Burn", "Shock", "Poison", "Corpse Explosion"):
                ctx.increase_stacks_pct(self.effects["buff"] / 100)

################################################################################
