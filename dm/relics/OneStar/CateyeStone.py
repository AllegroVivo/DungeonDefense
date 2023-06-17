from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, Context
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CateyeStone",)

################################################################################
class CateyeStone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-107",
            name="Cateye Stone",
            description=(
                "Inflicts damage to enemies as much as recovery canceled by Burn."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("burn_activated", self.notify)

################################################################################
    def notify(*args) -> None:
        """A general event response function."""

        pass

################################################################################
