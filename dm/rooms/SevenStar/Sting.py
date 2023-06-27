from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from dm.rooms.traproom import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Sting",)

################################################################################
class Sting(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-213",
            name="Sting",
            description=(
                "Once recharged, give {value} Poison to a random enemy in "
                "the adjacent area."
            ),
            level=level,
            rank=7,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Poison", base=64, per_lv=56)
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms + [self]:
            targets.extend(room.heroes)

        target = self.random.choice(targets)
        target.add_status("Poison", self.effects["Poison"], self)

################################################################################
