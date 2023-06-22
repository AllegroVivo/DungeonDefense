from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster  import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import HealingContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Cake",)

################################################################################
class Cake(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-188",
            name="Cake",
            description="Acquire 1 Defense each time LIFE is recovered.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_heal")

################################################################################
    def notify(self, ctx: HealingContext) -> None:
        """A general event response function."""

        # If the heal target is a monster...
        if isinstance(ctx.target, DMMonster):
            # Add 1 Defense.
            ctx.target.add_status("Defense", 1, self)

################################################################################
