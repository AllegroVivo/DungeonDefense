from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Haste",)

################################################################################
class Haste(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-147",
            name="Haste",
            description=(
                "DEX of deployed monster is increased by {value} %. Gives "
                "{status} Acceleration to deployed monsters whenever a hero "
                "enters the room."
            ),
            level=level,
            rank=4,
            effects=[
                Effect(name="DEX", base=10, per_lv=1),
                Effect(name="Acceleration", base=2, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Acceleration", self.effects["Acceleration"], self)

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("DEX", self.effects["DEX"] / 100)  # Convert to percentage

################################################################################
