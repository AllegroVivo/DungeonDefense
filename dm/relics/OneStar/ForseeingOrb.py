from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, Context
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ForseeingOrb",)

################################################################################
class ForseeingOrb(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-110",
            name="Forseeing Orb",
            description="Reduces LIFE consumed in Events by 20 %.",
            rank=1
        )

        # Not sure what to do until events are implemented.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this relic."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################
