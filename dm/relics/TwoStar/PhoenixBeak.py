from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.objects.monster import DMMonster
################################################################################

__all__ = ("PhoenixBeak",)

################################################################################
class PhoenixBeak(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-176",
            name="Phoenix's Beak",
            description=(
                "When more than 10 Acceleration is overlapped, effect of "
                "Acceleration increases by 50 %."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_applied")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:
        """A general event response function."""

        # If a monster is granted Acceleration
        if isinstance(ctx.target, DMMonster):
            # And the status being applied is Acceleration
            if ctx.status.name == "Acceleration":
                # Get the total number of stacks between the two statuses
                total_stacks = ctx.status.stacks
                acceleration = ctx.target.get_status("Acceleration")
                if acceleration is not None:
                    total_stacks += acceleration.stacks

                # And handle accordingly
                if total_stacks > 10:
                    ctx.status.amplify_pct(self.effect_value())

                    # Plus a little math to figure out where the stacks
                    # should be removed from.
                    if ctx.status.stacks > 10:
                        ctx.status.reduce_stacks_flat(10)
                    else:
                        diff = total_stacks - ctx.status.stacks
                        ctx.status.deplete_all_stacks()
                        acceleration.reduce_stacks_flat(diff)

################################################################################
