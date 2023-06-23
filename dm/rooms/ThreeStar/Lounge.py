from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Lounge",)

################################################################################
class Lounge(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-141",
            name="Lounge",
            description=(
                "Gives {value} ATK and {value} DEF to all monsters in the dungeon."
            ),
            level=level,
            rank=3,
            effects=[
                Effect(name="buff", base=4, per_lv=0.5),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.game.deployed_monsters:
            monster.increase_stat_flat("atk", self.effects["buff"])
            monster.increase_stat_flat("def", self.effects["buff"])

################################################################################
