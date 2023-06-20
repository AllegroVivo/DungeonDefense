from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LightningBolt",)

################################################################################
class LightningBolt(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-230",
            name="Lightning Bolt",
            description=(
                "Once recharged, inflict {damage} damage to 4 random enemies "
                "and give them {status} Shock."
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

        targets = random.sample(heroes, 4)

        for target in targets:
            target.damage(self.effect_value()[0])
            target.add_status("Shock", self.effect_value()[1])

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
        status = 40
        for _ in range(self.level):
            damage += random.randint(0, 80)
            status += 30

        return damage, status

################################################################################
