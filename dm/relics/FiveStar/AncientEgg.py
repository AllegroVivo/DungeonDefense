from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.game.day  import DMDay
################################################################################

__all__ = ("AncientEgg",)

################################################################################
class AncientEgg(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-291",
            name="Ancient Egg",
            description="You can feel the heartbeat of an unknown creature.",
            rank=5
        )

        self._start: int = self._state.day.current
        self._hits: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("day_advance")

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If the Dark Lord is targeted
        if ctx.defender == self.game.dark_lord:
            # And the attack hits
            if ctx.damage > 0:
                # Increment the hit counter
                self._hits += 1

        # If the hit counter reaches 1000
        if self._hits >= 1000:
            self.advance_relic("Broken Ancient Egg")

################################################################################
    def notify(self, day: DMDay) -> None:
        """A general event response function."""

        # If at least 100 days have passed
        if day.current - self._start >= 100:
            # Go to the next relic
            self.advance_relic("Elder Dragon")

################################################################################
    def advance_relic(self, relic: str) -> None:

        # Unsubscribe from event because the relic is about to be removed
        self.game.unsubscribe_event("day_advance", self.notify)
        # Add the specified new relic
        self.game.add_relic(relic)
        # Remove this relic
        self.game.relics.remove_relic(self)

################################################################################
