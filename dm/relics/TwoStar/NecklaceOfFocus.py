from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("NecklaceOfFocus",)

################################################################################
class NecklaceOfFocus(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-155",
            name="Necklace of Focus",
            description="Increases the effect of Focus to 100 %.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        if isinstance(ctx.target, DMHero):
            ctx.status.increase_base_effect(.50)  # Additional 50% to make 100%

################################################################################
