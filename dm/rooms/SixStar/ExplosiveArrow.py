from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ExplosiveArrow",)

################################################################################
class ExplosiveArrow(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-197",
            name="Explosive Arrow",
            description=(
                "Once recharged, inflict {value} damage to a random enemy in "
                "adjacent area and the enemies near it."
            ),
            level=level,
            rank=6
        )

        self.setup_charging(1.2, 1.2)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        # Grab a random target from the list of targets.
        target = random.choice(targets)
        # Then damage all heroes in the target's room.
        for hero in target.room.heroes:
            hero.damage(self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        A random value from the base damage range is chosen, then a random value
        from the additional damage range is added to the total for each level of
        this room.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        In this function:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 37)
        for _ in range(self.level):
            damage += random.randint(0, 36)

        return damage

################################################################################
