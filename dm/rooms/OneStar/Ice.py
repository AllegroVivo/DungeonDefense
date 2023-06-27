from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import Effect
from ..traproom import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Ice",)


################################################################################
class Ice(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-107",
            name="Ice",
            description=(
                "Inflicts {damage} damage and give {status} Slow to each hero "
                "that enters the room."
            ),
            level=level,
            rank=1,
            base_dmg=10,
            effects=[
                Effect(name="Slow", base=2, per_lv=1)
            ]
        )

    ################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.dmg)
        unit.add_status("Slow", self.effects["Slow"], self)

################################################################################
