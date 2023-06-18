from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import EggHatchContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Biography",)

################################################################################
class Biography(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-243",
            name="Biography",
            description="Pre-upgrades the next 5 monsters hatched from Eggs.",
            rank=4
        )

        self._uses = 5

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("egg_hatch", self.notify)

################################################################################
    def notify(self, ctx: EggHatchContext) -> None:
        """A general event response function."""

        # Upgrade all options
        for monster in ctx.options:
            monster.upgrade()

            # Increment the number of uses
            self._uses -= 1
            if self._uses <= 0:
                # Unsubscribe from the event if we're out of uses
                self.game.unsubscribe_event("egg_hatch", self.notify)

################################################################################
