from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom

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
            rank=1
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_flat("def", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base adjustment.
        - a is the additional effectiveness per level.
        - LV is the room's level.
        """

        return 4 + (2 * self.level)

################################################################################
