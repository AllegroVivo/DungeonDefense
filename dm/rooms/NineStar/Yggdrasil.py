from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Yggdrasil",)

################################################################################
class Yggdrasil(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-233",
            name="Yggdrasil",
            description=(
                "Once recharged, gives {value} Armor, Fury, and Regeneration "
                "to all monsters in the dungeon."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure,
            effects=[
                Effect(name="Status", base=60, per_lv=20),
            ]
        ),
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            for status in ("Armor", "Fury", "Regeneration"):
                monster.add_status(status, self.effects["Status"], self)

################################################################################
