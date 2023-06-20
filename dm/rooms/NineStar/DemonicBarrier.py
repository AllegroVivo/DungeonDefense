from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonicBarrier",)

################################################################################
class DemonicBarrier(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-222",
            name="Demonic Barrier",
            description=(
                "Once recharged, give {status} Shield and {status} Immune to "
                "all monsters in the dungeon. Monsters deployed in adjacent "
                "rooms will have their LIFE and DEF increased by {value} %."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth
        )

        self.setup_charging(6.6, 3.3)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Shield", self.effect_value()[0])
            monster.add_status("Immune", self.effect_value()[0])

################################################################################
    def effect_value(self) -> Tuple[int, float]:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        status = 1 + (1 * self.level)
        stat = (40 + (10 * self.level)) / 100  # Convert to percentage

        return status, stat

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.increase_stat_pct("LIFE", self.effect_value()[1])
            monster.increase_stat_pct("DEF", self.effect_value()[1])

################################################################################
