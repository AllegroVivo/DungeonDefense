from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..facilityroom import DMFacilityRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MeatWagon",)

################################################################################
class MeatWagon(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-201",
            name="Meat Wagon",
            description=(
                "Once recharged, give 2 (+1 per Lv) Immortality to adjacent monsters and get 5 (+1 per Lv) Gold."
            ),
            level=level,
            rank=6
        )

        self.setup_charging(20.0, 10.0)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.monsters)

        for target in targets:
            target.add_status("Immortality", self.effect_value()[0])

        self.game.inventory.add_gold(self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In these functions:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        status = 2 + (1 * self.level)
        gold = 5 + (1 * self.level)

        return status, gold

################################################################################
