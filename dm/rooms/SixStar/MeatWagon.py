from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..facilityroom import DMFacilityRoom
from utilities import Effect

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
                "Once recharged, give {status} Immortality to adjacent "
                "monsters and get {gold} Gold."
            ),
            level=level,
            rank=6,
            effects=[
                Effect(name="Immortality", base=2, per_lv=1),
                Effect(name="Gold", base=5, per_lv=1)
            ]
        )
        self.setup_charging(20.0, 10.0)

################################################################################
    def on_charge(self) -> None:

        # Apply Immortality to all monsters in adjacent rooms.
        for room in self.adjacent_rooms + [self]:
            for monster in room.monsters:
                monster.add_status("Immortality", self.effects["Immortality"], self)

        # Add gold.
        self.game.inventory.add_gold(self.effects["Gold"])

################################################################################
