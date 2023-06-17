from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MysteriousQuill",)

################################################################################
class MysteriousQuill(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-234",
            name="Mysterious Quill",
            description=(
                "The next 2 books to be acquired will be read immediately "
                "upon acquisition."
            ),
            rank=3,
            unlock=UnlockPack.Corruption
        )

        self._uses: int = 2

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("book_acquired", self.notify)

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        # Need to implement books first.
        self._uses += 1
        if self._uses >= 2:
            self.game.unsubscribe_event("book_acquired", self.notify)

################################################################################
