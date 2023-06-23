from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Graveyard",)

################################################################################
class Graveyard(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-132",
            name="Graveyard",
            description=(
                "Gives {value} Immortality to all monsters in the room at "
                "the beginning of the battle."
            ),
            level=level,
            rank=3,
            effects=[
                Effect(name="Immortality", base=2, per_lv=1),
            ]
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        for monster in self.monsters:
            monster.add_status("Immortality", self.effects["Immortality"], self)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("battle_start")

################################################################################
