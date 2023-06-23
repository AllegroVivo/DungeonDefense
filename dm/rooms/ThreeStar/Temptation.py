from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import Effect
from ..battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Temptation",)

################################################################################
class Temptation(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-140",
            name="Temptation",
            description=(
                "Give {value} Charm to hero that entered the room."
            ),
            level=level,
            rank=3,
            effects=[
                Effect(name="Charm", base=1, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Charm", self.effects["Charm"], self)

################################################################################
