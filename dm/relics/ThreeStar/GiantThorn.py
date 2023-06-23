from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm .core.contexts import StatusExecutionContext
################################################################################

__all__ = ("GiantThorn",)

################################################################################
class GiantThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-195",
            name="Giant Thorn",
            description="The damage from Thorn targets all the enemies in the room.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: StatusExecutionContext) -> None:

        # If we have a valid Thorn status
        if ctx.status.name == "Thorn":
            # And it was successful
            if ctx.stacks > 0:
                # And if the owner is a hero
                if isinstance(ctx.target, DMHero):
                    # Damage all the heroes in the room.
                    for hero in self.room.heroes:
                        hero.damage(ctx.stacks)

################################################################################
