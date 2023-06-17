from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("SpeedPotion",)

################################################################################
class SpeedPotion(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-165",
            name="Speed Potion",
            description="Increases the effect of Acceleration to 150 %.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Acceleration":
            if isinstance(status.owner, DMMonster):
                status.increase_base_effect(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 2.00  # Base effect of 50% + 200% (of 50%) = 150%

################################################################################
