from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

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
                "Once recharged, gives 60 (+20 per Lv) Armor, Fury, and "
                "Regeneration to all monsters in the dungeon."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure
        ),
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Armor", self.effect_value())
            monster.add_status("Fury", self.effect_value())
            monster.add_status("Regeneration", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 60 + (20 * self.level)

################################################################################
