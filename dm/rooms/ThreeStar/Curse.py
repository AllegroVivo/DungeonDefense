from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurseRoom",)

################################################################################
class CurseRoom(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-136",
            name="Curse",
            description=(
                "Inflicts {damage} damage, give {status} Weak, and {status} "
                "Vulnerable to the hero that entered the room."
            ),
            level=level,
            rank=3
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.damage(self.effect_value()[0])
                unit.add_status("Weak", self.effect_value()[1])
                unit.add_status("Vulnerable", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect.

        A random value from the base damage range is chosen, then a random value
        from the additional damage range is added to the total for each level of
        this room.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        **status = b + (a * LV)**

        In these functions:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - b is the base status.
        - a is the additional stacks per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 7)
        status = 2
        for _ in range(self.level):
            damage += random.randint(0, 6)
            status += 1

        return damage, status

################################################################################
