from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import GoldAcquiredContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BottomlessWallet",)

################################################################################
class BottomlessWallet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-246",
            name="Bottomless Wallet",
            description="Increases Gold acquisition by 20 %.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("gold_acquired")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################
    def notify(self, ctx: GoldAcquiredContext) -> None:
        """A general event response function."""

        ctx.amplify_pct(self.effect_value())

################################################################################
