from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Tailwind",)

################################################################################
class Tailwind(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-188",
            name="Tailwind",
            description=(
                "DEX of all monsters in the dungeon is increased by {value}."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original,
            effects=[
                Effect(name="dex", base=15, per_lv=1),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.increase_stat_pct("DEX", self.effects["dex"])

################################################################################
