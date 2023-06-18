from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CoreOfIce",)

################################################################################
class CoreOfIce(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-285",
            name="Core of Ice",
            description=(
                "All heroes' DEX is reduced by 1 %. Efficiency is gradually "
                "reduced on repeated acquisition."
            ),
            rank=4,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for hero in self.game.all_heroes:
            hero.reduce_stat_pct("dex", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b * (0.99^n)**

        In this function:

        - b is the base effectiveness.
        - n is the number of times this relic has been acquired.
        """

        return 0.01 * (0.99 ** self._count)

################################################################################
