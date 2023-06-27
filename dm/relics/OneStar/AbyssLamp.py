from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import TargetingContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssLamp",)

################################################################################
class AbyssLamp(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-101",
            name="Abyss Lamp",
            description=(
                "Enemies have a 10 % chance to attack another enemy, even if "
                "under the effect of Blind."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_target_acquire")

################################################################################
    def notify(self, ctx: TargetingContext) -> None:

        # Check for activation at a 10% chance.
        if self.random.chance(10):
            ctx.override(self.random.choice(self.room.heroes))

################################################################################
