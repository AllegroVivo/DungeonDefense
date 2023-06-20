from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import GoldAcquiredContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CorruptedAncientEgg",)

################################################################################
class CorruptedAncientEgg(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-335",
            name="Corrupted Ancient Egg",
            description="You can feel a dark energy.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

        self._souls_acquired: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("soul_acquired")

################################################################################
    def notify(self, ctx: GoldAcquiredContext) -> None:
        """A general event response function."""

        # Gold Context is a placeholder
        self._souls_acquired += ctx.calculate()

        if self._souls_acquired >= 10000:
            self.advance_relic()

################################################################################
    def advance_relic(self) -> None:
        # Unsubscribe from the event because the relic is about to be removed
        self.game.unsubscribe_event("soul_acquired", self.notify)
        # Add the upgraded relic
        self.game.add_relic("Corrupted Dragon")
        # Remove this relic
        self.game.relics.remove_relic(self)

################################################################################
