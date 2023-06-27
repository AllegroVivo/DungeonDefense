from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Infection",)

################################################################################
class Infection(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-187",
            name="Infection",
            description=(
                "Gives {value} Poison and Corpse Explosion to all heroes in "
                "the room whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="Status", base=24, per_lv=16),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for hero in self.heroes:
            for status in ("Poison", "Corpse Explosion"):
                hero.add_status(status, self.effects["Status"], self)

################################################################################
