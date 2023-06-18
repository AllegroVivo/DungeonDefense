from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SagesBrush",)

################################################################################
class SagesBrush(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-281",
            name="Sage's Brush",
            description=(
                "Every time you read, the Dark Lord's level increases by 1."
            ),
            rank=4,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("book_read", self.notify)

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        self.game.dark_lord.level_up(1)

################################################################################
