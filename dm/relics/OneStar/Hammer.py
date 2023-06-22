from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("Hammer",)

################################################################################
class Hammer(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-113",
            name="Hammer",
            description="Grants 1 extra Dull when the enemy is in Stun status.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if isinstance(ctx.target, DMHero):
            if ctx.status == "Dull":
                stun = ctx.target.get_status("Stun")
                if stun is not None:
                    ctx.status.increase_stacks_flat(1)

################################################################################
