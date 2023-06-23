from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import CorruptionContext
################################################################################

__all__ = ("BlackMask",)

################################################################################
class BlackMask(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-331",
            name="Black Mask",
            description="Cost of Corruption is reduced by 20 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("corruption_start")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################
    def notify(self, ctx: CorruptionContext) -> None:
        """A general event response function."""

        ctx.reduce_pct(self.effect_value())

################################################################################
