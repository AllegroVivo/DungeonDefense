from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

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
            rank=2,
            effects=[
                Effect(name="ATK", base=5, per_lv=5),
                Effect(name="DEF", base=5, per_lv=5),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_flat("ATK", self.effects["ATK"])
            monster.increase_stat_flat("DEF", self.effects["DEF"])

################################################################################
