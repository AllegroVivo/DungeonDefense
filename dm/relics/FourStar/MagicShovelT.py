from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MagicShovelT",)

################################################################################
class MagicShovelT(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-273",
            name="Magic Shovel (Top)",
            description="Add an extra Row to the top of the dungeon.",
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dungeon.extend_map(self)

################################################################################
