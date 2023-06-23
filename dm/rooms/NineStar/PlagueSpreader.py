from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PlagueSpreader",)

################################################################################
class PlagueSpreader(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-227",
            name="Plague Spreader",
            description=(
                "Once recharged, give {value} Poison and {value} Corpse "
                "Explosion to all enemies in adjacent area."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Poison", base=48, per_lv=36),
                Effect(name="Corpse Explosion", base=48, per_lv=36),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:
        """A general event response function."""

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        for target in targets:
            target.add_status("Poison", self.effects["Poison"], self)
            target.add_status("Corpse Explosion", self.effects["Corpse Explosion"], self)

################################################################################
