from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MagicGear",)

################################################################################
class MagicGear(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-142",
            name="Magic Gear",
            description=(
                "Once recharged, get {value} Gold."
            ),
            level=level,
            rank=3,
            effects=[
                Effect(name="Gold", base=5, per_lv=1),
            ]
        )

        self.setup_charging(charge_time=20.0, on_enter=2.0)

################################################################################
    def on_charge(self) -> None:

        self.game.inventory.add_gold(self.effects["Gold"])

################################################################################
