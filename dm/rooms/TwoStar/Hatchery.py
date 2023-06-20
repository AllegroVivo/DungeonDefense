from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom

if TYPE_CHECKING:
    from dm.core.contexts import EggHatchContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Hatchery",)

################################################################################
class Hatchery(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-130",
            name="Hatchery",
            description=(
                "Increases the level of monsters born from monster eggs by {value}."
            ),
            level=level,
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("egg_hatch")

################################################################################
    def notify(self, ctx: EggHatchContext) -> None:
        """A general event response function."""

        for monster in ctx.options:
            monster.level_up(self.effect_value())

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

        return 2 + (1 * self.level)

################################################################################
