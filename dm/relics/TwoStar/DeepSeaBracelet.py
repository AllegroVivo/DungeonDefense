from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import StatusExecutionContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DeepSeaBracelet",)

################################################################################
class DeepSeaBracelet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-171",
            name="Deep Sea Bracelet",
            description="The effect of Dull increases to 300 %.",
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Dull":
            if isinstance(ctx.status.owner, DMHero):
                ctx.status.increase_base_effect(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 2.00  # Additional 200 % to equal 300 %.

################################################################################
