from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("Rafflesia",)

################################################################################
class Rafflesia(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-256",
            name="Rafflesia",
            description=(
                "Apply 1 Corruption every time enemies take damage from Poison."
            ),
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Poison":
            status.owner.add_status("Corruption", 1)

################################################################################
