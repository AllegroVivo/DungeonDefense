from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("TheAbsolute",)

################################################################################
class TheAbsolute(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-196",
            name="The Absolute",
            description=(
                "Only one monster can be deployed. The deployed monsters' LIFE, "
                "ATK, DEF is increased by {value} % and default DEX is increased "
                "by 200 %."
            ),
            level=level,
            rank=6,
            monster_cap=1,
            unlock=UnlockPack.Advanced
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

        return (200 + (60 * self.level)) / 100

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:  # Only one, but this keeps it uniform.
            monster.increase_stat_pct("LIFE", self.effect_value())
            monster.increase_stat_pct("ATK", self.effect_value())
            monster.increase_stat_pct("DEF", self.effect_value())
            monster.increase_stat_pct("DEX", 2.00)

################################################################################
