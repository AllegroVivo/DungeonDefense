from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeathWave",)

################################################################################
class DeathWave(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-237",
            name="Death Wave",
            description=(
                "Once recharged, give {value} Poison and {value} Corpse "
                "Explosion to all enemies in the dungeon."
            ),
            level=level,
            rank=10,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Status", base=80, per_lv=40),
            ]
        )
        self.setup_charging(6.6, 3.3)

################################################################################
    def on_charge(self) -> None:

        for hero in self.game.all_heroes:
            for status in ("Poison", "Corpse Explosion"):
                hero.add_status(status, self.effects["Status"], self)

################################################################################
