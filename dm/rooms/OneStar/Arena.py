from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Arena",)

################################################################################
class Arena(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-102",
            name="Arena",
            description=(
                "The deployed monsters' ATK is increased by {value}."
            ),
            level=level,
            rank=1,
            effects=[
                Effect(name="atk", base=4, per_lv=2)
            ],
        )

################################################################################
    def stat_adjust(self) -> None:

        for monster in self.monsters:
            monster.increase_stat_flat("atk", self.effects["atk"])

################################################################################
