from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SwirlOfAnger",)

################################################################################
class SwirlOfAnger(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-215",
            name="Swirl of Anger",
            description=(
                "Once recharged, give {value} Fury and 1 Merciless to all "
                "monsters in adjacent area."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Fury", base=200, per_lv=200),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.add_status("Fury", self.effects["Fury"], self)
            monster.add_status("Merciless", 1, self)

################################################################################
