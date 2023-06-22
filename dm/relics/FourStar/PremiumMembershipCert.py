from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import PurchaseContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PremiumMembershipCert",)

################################################################################
class PremiumMembershipCert(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-255",
            name="Premium Membership Cert",
            description="Discounts price of items sold by Merchant by 15 %.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_purchase")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.15

################################################################################
    def notify(self, ctx: PurchaseContext) -> None:
        """A general event response function."""

        ctx.reduce_pct(self.effect_value())

################################################################################
