from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DoubleGiant",)

################################################################################
class DoubleGiant(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-146",
            name="Double Giant",
            description=(
                "You can deploy 2 monsters in this room, but the monsters will "
                "gigantify and get {life}x LIFE and {atk}x ATK."
            ),
            level=level,
            rank=4,
            monster_cap=2,
            effects=[
                Effect(name="life", base=2, per_lv=1),
            ]
        )

################################################################################
    @property
    def atk_boost(self) -> float:

        # Effectiveness every 10 levels after 6
        return float(2 + (1 * ((self.level - 6) // 10)))

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("life", self.effects["life"])
            monster.increase_stat_pct("attack", self.atk_boost)

################################################################################
