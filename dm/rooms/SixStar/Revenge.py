from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Revenge",)

################################################################################
class Revenge(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-202",
            name="Revenge",
            description=(
                "If monsters in adjacent rooms receive damage, get Fury as "
                "much as {value} % of ATK."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Fury", base=100, per_lv=10),
            ]
        )

        # I'm going to make the assumption that ATK represents the ATK of the
        # monster to whom the effect is being applied.

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if ctx.room in self.adjacent_rooms:
            ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            ctx.target.add_status("Fury", self.effects["Fury"] / 100 * ctx.source.attack, self)

################################################################################
