from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.objects.monster import DMMonster
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Flowerpot",)

################################################################################
class Flowerpot(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-249",
            name="Flowerpot",
            description=(
                "Get Fury as much as 100 % of LIFE healed from Regeneration."
            ),
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Regeneration":
            if isinstance(ctx.target, DMMonster):
                ctx.add_status("Fury", ctx.stacks)  # Regeneration heals are equal to stacks.

################################################################################
