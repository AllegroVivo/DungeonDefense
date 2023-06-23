from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

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
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="Shield", base=3, per_lv=1),
                Effect(name="Immune", base=3, per_lv=1),
                Effect(name="buff", base=40, per_lv=10)
            ]
        )
        self.setup_charging(6.6, 3.3)

################################################################################
    def on_charge(self) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Shield", self.effects["Shield"], self)
            monster.add_status("Immune", self.effects["Immune"], self)

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        monsters = []
        for room in self.adjacent_rooms:
            monsters.extend(room.monsters)

        for monster in monsters:
            monster.increase_stat_pct("life", self.effects["buff"] / 100)  # Convert to %
            monster.increase_stat_pct("def", self.effects["buff"] / 100)

################################################################################
