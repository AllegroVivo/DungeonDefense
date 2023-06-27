from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Pressure",)

################################################################################
class Pressure(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-149",
            name="Pressure",
            description=(
                "DEX of heroes in the room is decreased by {value} %. Gives "
                "{status} Slow to heroes that entered the room."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Original,
            effects=[
                Effect(name="DEX", base=10, per_lv=1),
                Effect(name="Slow", base=1, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.add_status("Slow", self.effects["Slow"], self)

################################################################################
    def stat_adjust(self) -> None:

        for hero in self.heroes:
            hero.reduce_stat_pct("DEX", self.effects["DEX"])

################################################################################
