from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PlagueSpreader",)

################################################################################
class PlagueSpreader(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-227",
            name="Plague Spreader",
            description=(
                "Once recharged, give {value} Poison and {value} Corpse "
                "Explosion to all enemies in adjacent area."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:
        """A general event response function."""

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        for target in targets:
            target.add_status("Poison", self.effect_value())
            target.add_status("Corpse Explosion", self.effect_value())

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

        return 48 + (36 * self.level)

################################################################################
