from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PoisonWeed",)

################################################################################
class PoisonWeed(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-205",
            name="Poison Weed",
            description=(
                "Increases Poison stat given by adjacent traps by {value} %."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced
        )

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

        return (100 + (5 * self.level)) / 100

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if ctx.attacker in self.adjacent_rooms:
            # Outgoing poison damage is increased
            pass

################################################################################
