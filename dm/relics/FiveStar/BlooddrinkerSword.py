from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts   import StatusExecutionContext
################################################################################

__all__ = ("BlooddrinkerSword",)

################################################################################
class BlooddrinkerSword(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-297",
            name="Blooddrinker Sword",
            description=(
                "Get 1 Hatred every time the Dark Lord's LIFE is restored by "
                "the effect of Vampire."
            ),
            rank=5
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.target == self.game.dark_lord:
            if ctx.status.name == "Vampire":
                self.game.dark_lord.add_status("Hatred", 1, self)

################################################################################
