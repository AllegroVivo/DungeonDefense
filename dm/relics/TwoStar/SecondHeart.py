from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SecondHeart",)

################################################################################
class SecondHeart(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-162",
            name="Second Heart",
            description=(
                "The Dark Lord revives with 100 % LIFE on death. (Only once)"
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If the dark lord is killed
        if ctx.target == self.game.dark_lord:
            # Revive will full life
            self.game.dark_lord.heal(self.game.dark_lord.max_life)
            # And unsubscribe so it only happens once.
            self.game.unsubscribe_event("on_death", self.notify)

################################################################################
