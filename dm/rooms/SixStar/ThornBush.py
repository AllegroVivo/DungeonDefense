from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ThornBush",)

################################################################################
class ThornBush(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-195",
            name="Thorn Bush",
            description=(
                "Gives {value} Armor Thorn to all monsters in adjacent rooms "
                "whenever a hero enters."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            targets = []
            for room in self.adjacent_rooms:
                targets.extend(room.monsters)

            for target in targets:
                target.add_status("Armor", self.effect_value())
                target.add_status("Thorn", self.effect_value())

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

        return 36 + (24 * self.level)

################################################################################
