from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("TheSeal",)

################################################################################
class TheSeal(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-214",
            name="The Seal",
            description=(
                "Once recharged, give {value} Shield and {value} Immune to all "
                "monsters in adjacent area."
            ),
            level=level,
            rank=7,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="status", base=3, per_lv=1)
            ]
        )
        self.setup_charging(3.3, 1.65)

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms + [self]:
            for monster in room.monsters:
                for status in ("Shield", "Immune"):
                    monster.add_status(status, self.effects["status"], self)

################################################################################
