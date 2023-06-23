from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Laboratory",)

################################################################################
class Laboratory(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-168",
            name="Laboratory",
            description=(
                "Collect {value} information every time an enemy enters the room. "
                "When 200 pieces of information are collected a random monster's "
                "rank is increased."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="information", base=1, per_lv=0.5),
            ]
        )

        self._information: float = 0.0

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        self._information += self.effects["information"]
        if self._information >= 100:
            self._information -= 100
            self.game.dungeon.upgrade_random_monster(include_inventory=True)

################################################################################
