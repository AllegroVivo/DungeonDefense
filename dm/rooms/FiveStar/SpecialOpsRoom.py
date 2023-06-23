from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SpecialOpsRoom",)

################################################################################
class SpecialOpsRoom(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-190",
            name="Special Ops Room",
            description=(
                "Increases damage inflicted to enemies by adjacent traps "
                "by {value} %."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="scalar", base=30, per_lv=2),
            ]
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        if ctx.source in self.adjacent_rooms:
            ctx.amplify_pct(self.effects["scalar"])

################################################################################
