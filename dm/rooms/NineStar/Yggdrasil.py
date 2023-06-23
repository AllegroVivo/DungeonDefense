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
                Effect(name="Armor", base=60, per_lv=20),
                Effect(name="Fury", base=60, per_lv=20),
                Effect(name="Regeneration", base=60, per_lv=20),
            ]
        ),
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Armor", self.effects["Armor"], self)
            monster.add_status("Fury", self.effects["Fury"], self)
            monster.add_status("Regeneration", self.effects["Regeneration"], self)

################################################################################
