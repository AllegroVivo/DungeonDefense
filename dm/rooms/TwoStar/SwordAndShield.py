from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SwordAndShield",)

################################################################################
class SwordAndShield(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-119",
            name="Sword and Shield",
            description=(
                "ATK and DEF of the deployed monsters are increased by {value}."
            ),
            level=level,
            rank=2
        )

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        A random value from the base effectiveness range is chosen, then a random
        value from the additional effectiveness range is added to the total for
        each level of this room.

        Breakdown:
        ----------
        **effect = b * (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 5 + (5 * self.level)

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_flat("atk", self.effect_value())
            monster.increase_stat_flat("def", self.effect_value())

################################################################################
