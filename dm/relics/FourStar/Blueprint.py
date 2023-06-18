from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import DMRoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Blueprint",)

################################################################################
class Blueprint(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-245",
            name="Blueprint",
            description=(
                "Increases the Dark Lord's DEF by 4 % per number of Traps "
                "deployed in the dungeon."
            ),
            rank=4
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.game.dark_lord.increase_stat_pct("defense", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b * t**

        In this function:

        - b is the base effectiveness.
        - t is the number of traps in the dungeon.
        """

        traps = [
            r for r in self.game.dungeon.all_rooms()
            if r.room_type is DMRoomType.Trap
        ]
        return 0.04 * len(traps)

################################################################################
