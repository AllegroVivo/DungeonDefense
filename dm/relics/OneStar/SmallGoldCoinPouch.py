from __future__ import annotations

import random

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SmallGoldCoinPouch",)

################################################################################
class SmallGoldCoinPouch(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-132",
            name="Small Gold Coin Pouch",
            description="Immediately acquire 100 - 500 Gold.",
            rank=1,
            unlock=UnlockPack.Advanced
        )

        self.count = 1

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.inventory.add_gold(random.randint(100, 500))

################################################################################
