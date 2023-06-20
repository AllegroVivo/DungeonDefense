from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Laboratory",)

################################################################################
class Laboratory(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-168",
            name="Laboratory",
            description=(
                "Collect {value} information every time an enemy enters the room. "
                "When 200 pieces of information are collected a random monster's "
                "rank is increased."
            ),
            level=level,
            rank=4
        )

        self._information: float = 0.0

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                self._information += self.effect_value()

        if self._information >= 100:
            self._information -= 100
            self.game.dungeon.upgrade_random_monster(include_inventory=True)

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

        return 1 + (0.5 * self.level)

################################################################################
