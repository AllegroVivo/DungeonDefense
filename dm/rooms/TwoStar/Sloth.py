from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sloth",)

################################################################################
class Sloth(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-127",
            name="Sloth",
            description=(
                "Gives {value} Weak and {value} Slow to all heroes that enter "
                "the room."
            ),
            level=level,
            rank=2
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.add_status("Weak", self.effect_value())
                unit.add_status("Slow", self.effect_value())

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

        return 3 + (1 * self.level)

################################################################################
