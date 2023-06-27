from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.monster import DMMonster
################################################################################

__all__ = ("BloodShield",)

################################################################################
class BloodShield(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-203",
            name="Blood Shield",
            description=(
                "If monsters in adjacent rooms receive damage, get Armor as "
                "much as {value} % of DEF."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Armor", base=500, per_lv=50),
            ]
        )

        # I'm going to make the assumption that DEF represents the DEF of the
        # monster to whom the effect is being applied.

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        if ctx.room in self.adjacent_rooms + [self]:
            if isinstance(ctx.target, DMMonster):
                ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            ctx.target.add_status(
                "Armor",
                (self.effects["Armor"] / 100) * ctx.target.defense,  # Convert to %
                self
            )

################################################################################
