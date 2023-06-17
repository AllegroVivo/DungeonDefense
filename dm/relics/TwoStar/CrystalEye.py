from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CrystalEye",)

################################################################################
class CrystalEye(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-181",
            name="Crystal Eye",
            description=(
                "You will instantly read 2 random Books that you have not "
                "completed reading."
            ),
            rank=2,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        # Read 2 random books. Once books are implemented.
        pass

################################################################################
