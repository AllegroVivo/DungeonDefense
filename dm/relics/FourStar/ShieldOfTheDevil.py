from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ShieldOfTheDevil",)

################################################################################
class ShieldOfTheDevil(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-270",
            name="Shield of the Devil",
            description=(
                "When a hero enters the Dark Lord's room, the Dark Lord "
                "gets 1 Shield."
            ),
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("room_enter", self.notify)

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self.game.dark_lord.room:
            self.game.dark_lord.add_status("Shield", 1)

################################################################################
