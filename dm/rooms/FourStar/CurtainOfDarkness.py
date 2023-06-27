from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurtainOfDarkness",)

################################################################################
class CurtainOfDarkness(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-155",
            name="Curtain of Darkness",
            description=(
                "Gives {blind} Blind to heroes that entered the room. Give "
                "{defense} Defense to all monsters in adjacent rooms at the "
                "beginning of the battle."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="Blind", base=1, per_lv=1),
                Effect(name="Defense", base=3, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("X", self.effects["X"], self)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        for room in self.adjacent_rooms:
            for monster in room.monsters:
                monster.add_status("X", self.effects["X"], self)

################################################################################
