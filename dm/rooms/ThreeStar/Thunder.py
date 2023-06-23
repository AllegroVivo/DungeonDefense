from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import Effect
from ..traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Thunder",)

################################################################################
class Thunder(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-139",
            name="Thunder",
            description=(
                "Inflicts {damage} damage and applies {status} Shock to a random "
                "hero in the dungeon when a hero enters the room."
            ),
            level=level,
            rank=3,
            base_dmg=18,
            effects=[
                Effect(name="Shock", base=16, per_lv=8),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        target = self.random.choice(self.game.dungeon.heroes)
        target.damage(self.damage)
        target.add_status("Shock", self.effects["Shock"], self)

################################################################################
