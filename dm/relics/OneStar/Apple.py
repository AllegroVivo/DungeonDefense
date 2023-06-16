from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Apple",)

################################################################################
class Apple(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-103",
            name="Apple",
            description="Increases all monsters' LIFE by 20%",
            rank=1
        )

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        for monster in self.game.all_monsters:
            monster.increase_stat_pct("life", 0.20)

################################################################################
