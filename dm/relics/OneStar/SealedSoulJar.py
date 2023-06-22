from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SealedSoulJar",)

################################################################################
class SealedSoulJar(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-129",
            name="Sealed Soul Jar",
            description="Obtain 30 - 100 souls.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.inventory.add_soul(self.random.from_range(30, 100))

################################################################################
