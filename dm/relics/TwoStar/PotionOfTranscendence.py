from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PotionOfTranscendence",)

################################################################################
class PotionOfTranscendence(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-158",
            name="Potion of Transcendence",
            description="Instantly trains all monsters.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        # Easy
        for monster in self.game.all_monsters:
            monster.upgrade()

################################################################################
