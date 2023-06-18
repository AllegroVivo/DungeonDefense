from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SacredScissors",)

################################################################################
class SacredScissors(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-271",
            name="Sacred Scissors",
            description="All heroes' ATK is reduced by 15 %.",
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for hero in self.game.all_heroes:
            hero.reduce_stat_pct("attack", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.15

################################################################################
