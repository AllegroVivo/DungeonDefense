from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CommandersGauntlet",)

################################################################################
class CommandersGauntlet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-189",
            name="Commander's Gauntlet",
            description=(
                "Increases the Dark Lord's ATK by 2 % per number of Battle "
                "Rooms placed in dungeon."
            ),
            rank=3
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.game.dark_lord.increase_stat_pct("attack", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b * r**

        In this function:

        - b is the base effectiveness.
        - r is the number of eligible rooms in the dungeon.
        """

        battle_rooms = [
            r for r in self.game.dungeon.all_rooms() if r.room_type is RoomType.Battle
        ]
        return 0.02 * len(battle_rooms)

################################################################################
