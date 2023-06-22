from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import PurchaseContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AncientCoin",)

################################################################################
class AncientCoin(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-237",
            name="Ancient Coin",
            description=(
                "Gold spent in shops is reduced by 1 %. Efficiency is gradually "
                "reduced on repeated acquisition."
            ),
            rank=3,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_purchase")

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
    def notify(self, ctx: PurchaseContext) -> None:
        """A general event response function."""

        ctx.reduce_pct(self.effect_value())

################################################################################
