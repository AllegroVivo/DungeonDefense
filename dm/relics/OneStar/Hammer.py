from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, Context
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("Hammer",)

################################################################################
class Hammer(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-113",
            name="Hammer",
            description="Grants 1 extra Dull when the enemy is in Stun status.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("dull_applied", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general receptor function for any argument-emitting events."""

        status.increase_stacks_flat(1)

################################################################################
