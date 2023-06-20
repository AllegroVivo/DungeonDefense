from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
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
                "will increase by 25 (+5 per Lv) %."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Myth
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

        return (25 + (5 * self.level)) / 100  # Convert to percentage.

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # Outgoing statuses are increased.
        pass

################################################################################
