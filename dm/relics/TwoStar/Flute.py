from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("Flute",)

################################################################################
class Flute(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-173",
            name="Flute",
            description="Get 3 Focus when Absorption is activated.",
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

        if status.name == "Absorption":
            if isinstance(status.owner, DMMonster):
                if status.stacks > 0:
                    status.owner.add_status("Focus", stacks=3)

################################################################################
