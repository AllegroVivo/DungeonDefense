from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.objects.status import DMStatus
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("RingOfWeakness",)

################################################################################
class RingOfWeakness(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-160",
            name="Ring of Weakness",  # Originally said "50%", but base effectiveness is 50%, so...
            description="Increases the effect of Weak to 60 %.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Weak":
            if isinstance(status.owner, DMHero):
                status.increase_base_effect(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################
