from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CurseWave",)

################################################################################
class CurseWave(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-218",
            name="Curse Wave",
            description=(
                "Once recharged, give {value} Weak, Vulnerable, and Curse to "
                "all enemies in adjacent area."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Status", base=3, per_lv=1),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms:
            for hero in room.heroes:
                for status in ("Weak", "Vulnerable", "Curse"):
                    hero.add_status(status, self.effects["Status"], self)

################################################################################
