from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("RingOfEnlightenment",)

################################################################################
class RingOfEnlightenment(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-235",
            name="Ring of Enlightenment",
            description=(
                "Every time you finish reading a Book, the level of all monsters "
                "increases by 3."
            ),
            rank=3,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("book_completed")

################################################################################
    def notify(self, book: DMBook) -> None:  # type: ignore
        """A general event response function."""

        for monster in self.game.all_monsters:
            monster.level_up(3)

################################################################################
