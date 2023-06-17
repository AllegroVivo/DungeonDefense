from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("HiddenBox",)

################################################################################
class HiddenBox(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-148",
            name="Hidden Box",
            description=(
                "Has a small chance to acquire extra battle rewards in "
                "boss battles."
            ),
            rank=2
        )

        # Need to implement in reward logic maybe? Small chance is 20%.

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
