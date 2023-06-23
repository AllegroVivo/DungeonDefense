from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Warhorn",)

################################################################################
class Warhorn(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-157",
            name="Warhorn",
            description=(
                "Gives {value} Fury to all monsters in the dungeon when "
                "a hero enters."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Fury", base=16, per_lv=8),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Fury", self.effects["Fury"], self)

################################################################################
