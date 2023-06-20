from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BrokenAncientEgg",)

################################################################################
class BrokenAncientEgg(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-293",
            name="Broken Ancient Egg",
            description="All monsters' combat ability decreases by 5 %.",
            rank=5
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.game.deployed_monsters:
            monster.reduce_stat_pct("combat", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.05

################################################################################
