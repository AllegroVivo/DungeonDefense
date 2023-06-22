from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("InsigniaOfTerror",)

################################################################################
class InsigniaOfTerror(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-114",
            name="Insignia of Terror",
            description=(
                "Gives 1 Panic to the hero that landed on a trap for the first time."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("trap_activated", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If we're a hero
        if isinstance(ctx.target, DMHero):
            # And we're being attacked by a trap
            if isinstance(ctx.source, DMTrapRoom):
                #  And the trap hasn't been activated before
                if not ctx.source.activated_before:
                    # Add status effect
                    ctx.target.add_status("Panic")
                    # Remember to mark the trap as activated.
                    ctx.source.activate_first_time()

################################################################################
