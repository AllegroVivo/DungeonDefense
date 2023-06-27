from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElectricField",)

################################################################################
class ElectricField(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-156",
            name="Electric Field",
            description=(
                "Gives {value} Shock to all heroes in adjacent rooms when "
                "a hero enters the room."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Shock", base=36, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for room in self.adjacent_rooms + [self]:
            for hero in room.heroes:
                hero.add_status("Shock", self.effects["Shock"], self)

################################################################################
