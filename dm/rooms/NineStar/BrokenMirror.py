from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BrokenMirror",)

################################################################################
class BrokenMirror(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-231",
            name="Broken Mirror",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in "
                "adjacent room and give them {status} Haze. Inflict {value} % "
                "extra damage by consuming 1 Mirror if the target is under "
                "effect of Mirror."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_charge(self) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        for hero in heroes:
            hero.damage(self.effect_value()[0])
            hero.add_status("Haze", self.effect_value()[1])
            mirror = hero.get_status("Mirror")
            if mirror is not None:
                hero.damage(self.effect_value()[0] * self.effect_value()[2])
                mirror.reduce_stacks_flat(1)

################################################################################
    def effect_value(self) -> Tuple[int, int, float]:
        """The value(s) of this room's effect(s).

        A random value from the base damage range is chosen, then a random value
        from the additional damage range is added to the total for each level of
        this room.

        Breakdown:
        ----------
        **damage = (i to j) + ((x to y) * LV)**

        **status/dmg_buff = b + (a * LV)**

        In these functions:

        - (i to j) is the base damage.
        - (x to y) is the additional damage per level.
        - b is the base amount.
        - a is the additional amount per level.
        - LV is the level of this room.
        """

        damage = random.randint(1, 121)
        status = 5
        buff = 400

        for _ in range(self.level):
            damage += random.randint(0, 120)
            status += 1
            buff += 4

        return damage, status, (buff / 100)  # Convert to percentage.

################################################################################