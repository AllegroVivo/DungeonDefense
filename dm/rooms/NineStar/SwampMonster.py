from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwampMonster",)

################################################################################
class SwampMonster(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-232",
            name="Swamp Monster",
            description=(
                "Inflict  {damage} damage to entering heroes, while reducing "
                "target's Armor by 50 % and giving {status} Slow."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            unit.damage(self.effect_value()[0])
            unit.add_status("Slow", self.effect_value()[1])
            armor = unit.get_status("Armor")
            if armor is not None:
                armor.reduce_stacks_pct(0.50)

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

        damage = random.randint(1, 91)
        status = 5
        for _ in range(self.level):
            damage += random.randint(90, 180)
            status += 1

        return damage, status

################################################################################
