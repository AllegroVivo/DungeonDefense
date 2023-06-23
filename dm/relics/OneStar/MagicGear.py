from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MagicGear",)

################################################################################
class MagicGear(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-119",
            name="Magic Gear",
            description="Immediately upgrades 2 random facilities.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        options = self.game.dungeon.all_rooms()
        if len(options) == 0:
            return

        results = self.random.sample(options, k=2)
        for room in results:
            room.upgrade()

################################################################################
