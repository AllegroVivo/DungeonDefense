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

__all__ = ("ChainLightning",)

################################################################################
class ChainLightning(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-182",
            name="Chain Lightning",
            description=(
                "Give {value} Shock to 5 nearby enemies and the hero that "
                "entered the room when a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original
        )

        # Note: Also deals 1~34 (+0~23 per Lv) damage.
        # Will assume it's toward all targets.

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            rooms = self.game.dungeon.get_adjacent_rooms(self.position, include_current=True)
            heroes = []
            for room in rooms:
                heroes.extend(room.heroes)

            # Remove the unit so we can select 5 targets in addition to the triggering hero.
            heroes.remove(unit)  # type: ignore

            # Select 5 targets.
            targets = random.sample(heroes, 5)
            # Add the triggering hero back to the list.
            targets.append(unit)

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

        damage = random.randint(1, 34)
        status = 32
        for _ in range(self.level):
            damage += random.randint(0, 23)
            status += 24

        return damage, status

################################################################################
