from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FrostyWind",)

################################################################################
class FrostyWind(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-189",
            name="Frosty Wind",
            description=(
                "DEX of all heroes in the dungeon is decreased by {value}."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="dex", base=10, per_lv=1),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:

        for hero in self.game.all_heroes:
            hero.reduce_stat_pct("dex", self.effects["dex"] / 100)  # Convert to percentage

################################################################################
