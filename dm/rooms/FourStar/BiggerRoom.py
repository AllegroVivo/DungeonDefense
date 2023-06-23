from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import UnlockPack, Effect
from ..battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BiggerRoom",)


################################################################################
class BiggerRoom(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):
        super().__init__(
            game, position,
            _id="ROOM-150",
            name="Bigger Room",
            description=(
                "Increases the number of deployable monsters by 1. The deployed "
                "monsters' LIFE is increased by {value} %."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening,
            monster_cap=4,
            effects=[
                Effect(name="life", base=50, per_lv=25),
            ]
        )

    ################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("LIFE", self.effects["life"] / 100)  # Convert to percentage

################################################################################
