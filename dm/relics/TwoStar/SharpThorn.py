from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("SharpThorn",)

################################################################################
class SharpThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-163",
            name="Sharp Thorn",
            description="Damage dealt with Thorn cannot be absorbed.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMHero):
            if ctx.status.name == "Thorn":
                ctx.set_direct_damage(True)

################################################################################
