from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("Net",)

################################################################################
class Net(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-156",
            name="Net",
            description="Increases the effect of Slow to 60 %.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Slow":
            if isinstance(status.owner, DMHero):
                status.increase_base_effect(0.20)  # Base effect of 50% + 20% = 60%

################################################################################

