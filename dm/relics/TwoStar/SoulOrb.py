from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("SoulOrb",)

################################################################################
class SoulOrb(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-177",
            name="Soul Orb",
            description="Get 1 Shield when Immortality is triggered.",
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Immortality":
            if status.stacks > 0:
                status.owner.add_status("Shield", stacks=1)

################################################################################
