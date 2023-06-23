from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import UnlockPack, Effect
from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("IcePit",)

################################################################################
class IcePit(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-165",
            name="IcePit",
            description=(
                "When a hero enters, give {damage} damage, disable movement "
                "for a while, and give {status} Slow to all enemies in the room."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening,
            base_dmg=46,
            effects=[
                Effect(name="Slow", base=1, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)
        unit.immobilize(1.5)

        for hero in self.heroes:
            hero.add_status("Slow", self.effects["Slow"], self)

################################################################################
