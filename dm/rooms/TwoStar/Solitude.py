from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import RoomType, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Solitude",)

################################################################################
class Solitude(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-117",
            name="Solitude",
            description=(
                "ATK of monsters deployed in this room increases by {value} per "
                "number of rooms in the dungeon that are not battle rooms."
            ),
            level=level,
            rank=2,
            effects=[
                Effect(name="ATK", base=4, per_lv=4),
            ]
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        rooms = [
            r for r in self.game.dungeon.all_rooms()
            if r.room_type is not RoomType.Battle
        ]

        for monster in self.monsters:
            monster.increase_stat_flat("ATK", self.effects["ATK"] * len(rooms))

################################################################################
