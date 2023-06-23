from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StigmaOfDragonSlayer",)

################################################################################
class StigmaOfDragonSlayer(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-301",
            name="Stigma of Dragon Slayer",
            description="A dragon slayer's declaration of war.",
            rank=5
        )

        # This relic is removed if the Dragon Slayer is captured. Will have to work that later.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        # Tell the battle manager to include the Dragon Slayer in spawns.
        self.game.battle_mgr.set_dragon_slayer(True)

################################################################################
