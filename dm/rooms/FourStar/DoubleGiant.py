from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom

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
            monster_cap=2
        )

################################################################################
    def effect_value(self) -> Tuple[float, float]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **life = b + (a * LV)**

        **atk = b + (a * LV@10(6))**

        In these functions:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        - LV@10(6) represents every 10 levels after the 6th level.
        """

        life = float(2 + (1 * self.level))
        attack = float(2 + (1 * ((self.level - 6) // 10)))  # Effectiveness every 10 levels after 6

        return life, attack

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("life", self.effect_value()[0])
            monster.increase_stat_pct("attack", self.effect_value()[1])

################################################################################
