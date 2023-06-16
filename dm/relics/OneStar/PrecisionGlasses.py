from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PrecisionGlasses",)

################################################################################
class PrecisionGlasses(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-128",
            name="Precision Glasses",
            description="All rooms gain a small amount of EXP.",
            rank=1
        )

        self.count = 1

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        for room in self.game.dungeon.all_rooms():
            room.grant_exp(room.level * 100)  # Probably need to experiment with this value.

################################################################################
