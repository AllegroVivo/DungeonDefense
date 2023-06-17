from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import DMRoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonSword",)

################################################################################
class DemonSword(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-141",
            name="Demon Sword",
            description=(
                "All monsters' ATK is increased by 20% for every Shrine "
                "placed in the dungeon."
            ),
            rank=2
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        count = 0
        for room in self.game.dungeon.all_rooms():
            if room.type is DMRoomType.Shrine:
                count += 1

        for monster in self.game.deployed_monsters:
            monster.increase_stat_pct("attack", count * 0.20)

################################################################################
