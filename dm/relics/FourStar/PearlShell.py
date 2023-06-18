from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("PearlShell",)

################################################################################
class PearlShell(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-268",
            name="Pearl Shell",
            description=(
                "Whenever Slow is inflicted on an enemy, also inflict 1 Frostbite."
            ),
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_acquired", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Slow":
            if isinstance(status.owner, DMHero):
                status.owner.add_status("Frostbite", 1)

################################################################################
