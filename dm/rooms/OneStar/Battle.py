from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Battle",)

################################################################################
class Battle(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-101",
            name="Battle",
            description=(
                "Deployed monsters' maximum LIFE is increased by {value}."
            ),
            level=level,
            rank=1,
            effects=[
                Effect(name="life", base=25, per_lv=5)
            ],
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_flat("life", self.effects["life"])

################################################################################
