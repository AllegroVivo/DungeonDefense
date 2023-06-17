from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("PhoenixBeak",)

################################################################################
class PhoenixBeak(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-176",
            name="Phoenix's Beak",
            description=(
                "When more than 10 Acceleration is overlapped, effect of "
                "Acceleration increases by 50 %."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_acquire", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Acceleration":
            if status.stacks > 10:
                status.amplify_pct(self.effect_value())

################################################################################
