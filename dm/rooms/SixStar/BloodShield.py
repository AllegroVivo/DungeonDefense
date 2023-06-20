from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from ...core.objects.monster import DMMonster
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
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
            unlock=UnlockPack.Advanced
        )

        # I'm going to make the assumption that DEF represents the DEF of the
        # monster to whom the effect is being applied.

################################################################################
    def effect_value(self) -> float:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return (500 + (50 * self.level)) / 100

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.defender, DMMonster):
            adj_monsters = []
            for room in self.adjacent_rooms:
                adj_monsters.extend(room.monsters)

            if ctx.defender in adj_monsters:
                ctx.defender.add_status("Armor", self.effect_value() * ctx.defender.defense)

################################################################################
