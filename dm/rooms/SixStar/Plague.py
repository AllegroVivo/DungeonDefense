from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack


if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Plague",)

################################################################################
class Plague(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-200",
            name="Plague",
            description=(
                "Gives {value} Poison and Corpse Explosion to all heroes in "
                "adjacent rooms whenever a hero enters the room."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
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

        return 24 + (16 * self.level)

################################################################################
