from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import StatusApplicationContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BlossomingFlame",)

################################################################################
class BlossomingFlame(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-204",
            name="Blossoming Flame",
            description=(
                "Increases Burn stat given by adjacent traps by {value} %."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="buff", base=100, per_lv=5),
            ]
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if ctx.source in self.adjacent_rooms:
            if ctx.status.name == "Burn":
                ctx.increase_stacks_pct(self.effects["buff"] / 100)

################################################################################
