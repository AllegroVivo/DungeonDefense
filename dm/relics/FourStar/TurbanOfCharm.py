from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TurbanOfCharm",)

################################################################################
class TurbanOfCharm(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-259",
            name="Turban of Charm",
            description=(
                "Gives 1 Charm to heroes that entered the Dark Lord's Room."
            ),
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("room_enter", self.notify)

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self.game.dark_lord.room:
            unit.add_status("Charm")

################################################################################
