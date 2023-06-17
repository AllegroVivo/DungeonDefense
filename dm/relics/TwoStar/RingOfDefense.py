from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.objects.status import DMStatus
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("RingOfDefense",)

################################################################################
class RingOfDefense(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-159",
            name="Ring of Defense",
            description="Increases the effect of Defense to 60 %.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Defense":
            if isinstance(status.owner, DMMonster):
                status.increase_base_effect(0.20)  # Base effect of 50% + 20% (of 50%) = 60%

################################################################################
