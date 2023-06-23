from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import CorruptionContext
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

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("corruption_start")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b * (0.99^n)**

        In this function:

        - b is the base effectiveness.
        - n is the number of times this relic has been acquired.
        """

        return 0.50 * (0.02 ** self._count)

################################################################################
    def notify(self, ctx: CorruptionContext) -> None:

        ctx.reduce_pct(self.effect_value())

################################################################################
