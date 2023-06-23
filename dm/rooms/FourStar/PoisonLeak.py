from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PoisonLeak",)

################################################################################
class PoisonLeak(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-162",
            name="Poison Leak",
            description=(
                "Gives {value} Poison to all enemies in all adjacent rooms "
                "when a hero enters the room."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Poison", base=32, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.get_heroes_or_monsters(unit))
            for target in targets:
                target.add_status("Poison", self.effects["Poison"], self)

################################################################################
