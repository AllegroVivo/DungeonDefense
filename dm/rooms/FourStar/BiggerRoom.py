from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero
from utilities  import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
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
            monster_cap=4
        )

################################################################################
    def effect_value(self) -> float:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 0.50 + (0.25 * self.level)

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("life", self.effect_value())

################################################################################
