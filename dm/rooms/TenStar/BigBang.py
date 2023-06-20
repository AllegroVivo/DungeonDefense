from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BigBang",)

################################################################################
class BigBang(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-235",
            name="Big Bang",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in the "
                "dungeon, and apply them {status} Burn and {status} Shock."
            ),
            level=level,
            rank=10,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(6.6, 6.6)

################################################################################
    def on_charge(self) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.effect_value()[0])
            hero.add_status("Burn", self.effect_value()[1])
            hero.add_status("Shock", self.effect_value()[1])

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

        damage = random.randint(1, 121)
        status = 80
        for _ in range(self.level):
            damage += random.randint(0, 120)
            status += 40

        return damage, status

################################################################################