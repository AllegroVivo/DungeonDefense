from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ThreeGiganteers",)

################################################################################
class ThreeGiganteers(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-170",
            name="Three Giganteers",
            description=(
                "Deployed monsters will gigantify and get {life}x LIFE "
                "and {atk}x ATK."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original
        )

################################################################################
    def effect_value(self) -> Tuple[float, float]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        life = float(2 + (1 * self.level))
        attack = float(2 + (1 * ((self.level - 4) // 5)))  # Effectiveness every 5 levels after 4

        return life, attack

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("life", self.effect_value()[0])
            monster.increase_stat_pct("attack", self.effect_value()[1])

################################################################################
