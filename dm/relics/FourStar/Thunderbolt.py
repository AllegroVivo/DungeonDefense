from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.status    import DMStatus
################################################################################

__all__ = ("Thunderbolt",)

################################################################################
class Thunderbolt(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-282",
            name="Thunderbolt",
            description="Additional damage caused by Shock is increased by 75 %.",
            rank=4,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_execute", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.75

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Shock":
            status.increase_base_effect(self.effect_value())

################################################################################
