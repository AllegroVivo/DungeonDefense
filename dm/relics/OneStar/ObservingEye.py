from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ObservingEye",)

################################################################################
class ObservingEye(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-121",
            name="Observing Eye",
            description="No more enemies will show up in Events.",
            rank=1
        )

        # Need to implement Events first to figure out specifics.

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
        """Called automatically when a stat refresh is initiated."""

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
