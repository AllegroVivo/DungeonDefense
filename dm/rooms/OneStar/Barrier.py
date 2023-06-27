from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import Effect
from ..battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Barrier",)

################################################################################
class Barrier(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-103",
            name="Barrier",
            description="The deployed monster's DEF is increased by {value}.",
            level=level,
            rank=1,
            effects=[
                Effect(name="def", base=4, per_lv=2)
            ]
        )

################################################################################
    def stat_adjust(self) -> None:

        for monster in self.monsters:
            monster.increase_stat_flat("def", self.effects["def"])

################################################################################
