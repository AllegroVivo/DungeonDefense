from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CorruptionController",)

################################################################################
class CorruptionController(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-332",
            name="Corruption Controller",
            # description=(  # Original phrasing
            #     "Reduces the increment of Corruption cost based on the number "
            #     "of corrupted heroes you own by 50 %."
            # ),
            description=(
                "Reduces the cost of Corruption by 50% with increasing "
                "effectiveness based on the number of corrupted heroes you own."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

        # Will look at this once I've got Corruption working.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (e * s)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per stack.
        - s is the number of Acceleration stacks.
        """

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################
