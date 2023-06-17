from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import DMRoomType, UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.room import DMRoom
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DragonKingsBelt",)

################################################################################
class DragonKingsBelt(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-172",
            name="Dragon King's Belt",
            description=(
                "If a hero leaves a Battle Room without Dull, hero gets 1 Dull."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("room_exit", self.notify)

################################################################################
    def notify(self, unit: DMUnit, room: DMRoom) -> None:
        """A general event response function."""

        if room.room_type is DMRoomType.Battle:
            dull = unit.get_status("Dull")
            if dull is None:
                unit.add_status("Dull")

################################################################################
