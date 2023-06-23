from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("InfinityClock",)

################################################################################
class InfinityClock(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-225",
            name="Infinity Clock",
            description=(
                "Boost DEX of monsters in adjacent rooms by {value} %, and "
                "when hero enters, give {status} Acceleration to monsters in "
                "adjacent rooms."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure,
            effects=[
                Effect(name="Acceleration", base=5, per_lv=1),
                Effect(name="dex", base=100, per_lv=4),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        if unit.room == self:
            monsters = []
            for room in self.adjacent_rooms:
                monsters.extend(room.monsters)

            for monster in monsters:
                monster.add_status("Acceleration", self.effects["Acceleration"], self)

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.increase_stat_pct("dex", self.effects["dex"] / 100)  # Convert to %

################################################################################
