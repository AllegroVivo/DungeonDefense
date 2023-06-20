from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Foundry",)

################################################################################
class Foundry(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-192",
            name="Foundry",
            description=(
                "Increases DEF of monsters in adjacent rooms by {value}%."
            ),
            level=level,
            rank=5,
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

        return (30 + (2 * self.level)) / 100  # Convert to percentage.

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.monsters)

        for monster in targets:
            monster.increase_stat_pct("def", self.effect_value())

################################################################################
