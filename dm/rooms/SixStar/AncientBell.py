from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AncientBell",)

################################################################################
class AncientBell(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-208",
            name="Ancient Bell",
            description=(
                "Once recharged, give {value} Focus to all monsters in "
                "adjacent area."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Focus", base=10, per_lv=2),
            ]
        )

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms + [self]:
            for monster in room.monsters:
                monster.add_status("Focus", self.effects["Focus"], self)

################################################################################
