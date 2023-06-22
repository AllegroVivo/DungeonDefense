from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import EggHatchContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MonsterNest",)

################################################################################
class MonsterNest(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-253",
            name="Monster Nest",
            description="The Hatchery's effect increases by 50 %.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("egg_hatch")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
    def notify(self, ctx: EggHatchContext) -> None:

        pass

################################################################################
