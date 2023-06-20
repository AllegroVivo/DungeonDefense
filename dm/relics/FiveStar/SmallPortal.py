from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SmallPortal",)

################################################################################
class SmallPortal(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-300",
            name="Small Portal",
            description="Enemies will enter the dungeon less frequently.",
            rank=5
        )

        # -30% entry rate per the wiki

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dungeon.modify_hero_spawn_rate(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return -0.30

################################################################################
