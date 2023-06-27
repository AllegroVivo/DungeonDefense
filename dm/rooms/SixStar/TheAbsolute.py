from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

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
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="buff", base=200, per_lv=60),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:  # Only one, but this keeps it uniform.
            monster.increase_stat_pct("DEX", 2.00)
            for stat in ("LIFE", "ATK", "DEF"):
                monster.increase_stat_pct(stat, self.effects["buff"])

################################################################################
