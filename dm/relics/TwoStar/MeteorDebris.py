from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("MeteorDebris",)

################################################################################
class MeteorDebris(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-175",
            name="Meteor Debris",
            description=(
                "When granting Burn to a hero in Armor status, the target's "
                "Armor decrease by 30 % of the granted stat."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("status_acquire", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Burn":
            armor = status.owner.get_status("Armor")
            if armor is not None:
                armor.reduce_stacks_flat(int(status.stacks * 0.30))

################################################################################
