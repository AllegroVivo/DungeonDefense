from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManaPotion",)

################################################################################
class ManaPotion(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-152",
            name="Mana Potion",
            description="Acquire 3 Mana Crystals.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dark_lord.increase_max_mana(3)

################################################################################
