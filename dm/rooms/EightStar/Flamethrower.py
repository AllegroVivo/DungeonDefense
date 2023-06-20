from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Flamethrower",)

################################################################################
class Flamethrower(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-219",
            name="Flamethrower",
            description=(
                "Once recharged, inflict {damage} damage to a random enemy "
                "in the adjacent area and the enemies near it, and give "
                "them {status} Burn."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:
        """A general event response function."""

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        target = random.choice(targets)
        target.damage(self.effect_value()[0])
        target.add_status("Burn", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect(s).

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

        damage = random.randint(1, 81)
        status = 72
        for _ in range(self.level):
            damage += random.randint(0, 80)
            status += 48

        return damage, status

################################################################################
