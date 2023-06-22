from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities       import RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BackwardsClock",)

################################################################################
class BackwardsClock(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-261",
            name="Backwards Clock",
            description="Remove 1 random Shrine.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        shrines = [r for r in self.game.dungeon.all_rooms() if r.room_type is RoomType.Shrine]
        target = self.random.choice(shrines)
        target.remove()

################################################################################
