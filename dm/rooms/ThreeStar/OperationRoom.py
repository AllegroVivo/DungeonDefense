from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("OperationRoom",)

################################################################################
class OperationRoom(DMFacilityRoom):

    AREA_TRAPS = (
        "Explosion"
    )

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-143",
            name="Operation Room",
            description=(
                "All traps' ATK is increased by {value}. However, the efficiency "
                "is reduced for traps that attack multiple enemies simultaneously."
            ),
            level=level,
            rank=3
        )

        # Will need to revisit this one.

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 8 + (6 * self.level)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # Need to figure this out a little more when I actually make traps attack.
        if isinstance(ctx.source, DMTrapRoom):
            ctx.source.attack_power += self.effect_value()

        # Also need to reduce effectiveness somehow?

################################################################################
