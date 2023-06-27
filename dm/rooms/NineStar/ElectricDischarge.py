from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ElectricDischarge",)

################################################################################
class ElectricDischarge(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-226",
            name="Electric Discharge",
            description=(
                "Once recharged, give {value} Shock to all enemies in "
                "adjacent area."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Shock", base=52, per_lv=42),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms:
            for hero in room.heroes:
                hero.add_status("Shock", self.effects["Shock"], self)

################################################################################
