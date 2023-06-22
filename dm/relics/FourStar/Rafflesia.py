from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.objects.hero    import DMHero
################################################################################

__all__ = ("Rafflesia",)

################################################################################
class Rafflesia(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-256",
            name="Rafflesia",
            description=(
                "Apply 1 Corruption every time enemies take damage from Poison."
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

        ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        # If the status is Poison
        if ctx.status.name == "Poison":
            # And it's being applied to a hero
            if isinstance(ctx.target, DMHero):
                # Apply Corruption as well
                ctx.add_status("Corruption", 1)

################################################################################
