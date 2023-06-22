from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts   import StatusExecutionContext
################################################################################

__all__ = ("WoodenStaff",)

################################################################################
class WoodenStaff(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-224",
            name="Wooden Staff",
            description="Get Armor equal to 20 % of LIFE healed by Regeneration.",
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        # If we're a monster
        if isinstance(ctx.target, DMMonster):
            # And the Regeneration status was executed
            if ctx.status.name == "Regeneration":
                # Add 20 % of the LIFE healed by Regeneration as Armor.
                ctx.target.add_status("Armor", ctx.stacks * 0.20, self)

################################################################################
