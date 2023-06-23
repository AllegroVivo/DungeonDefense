from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("IronSkin",)

################################################################################
class IronSkin(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-234",
            name="Iron Skin",
            description=(
                "Once recharged, give {value} Armor and {value} Thorn to all "
                "monsters in adjacent area."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Armor", base=128, per_lv=96),
                Effect(name="Thorn", base=128, per_lv=96),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.add_status("Armor", self.effects["Armor"], self)
            monster.add_status("Thorn", self.effects["Thorn"], self)

################################################################################
