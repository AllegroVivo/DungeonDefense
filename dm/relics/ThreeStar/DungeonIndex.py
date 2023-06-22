from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import RoomSpawnContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DungeonIndex",)

################################################################################
class DungeonIndex(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-192",
            name="Dungeon Index",
            description="The next 2 Facilities you acquire will be pre-upgraded.",
            rank=3
        )

        self._upgrades: int = 2

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("room_spawn")

################################################################################
    def notify(self, ctx: RoomSpawnContext) -> None:
        """A general event response function."""

        if self._upgrades > 0:
            ctx.room.upgrade()
            self._upgrades -= 1

        if self._upgrades <= 0:
            self.game.unsubscribe_event("room_spawn", self.notify)

################################################################################
