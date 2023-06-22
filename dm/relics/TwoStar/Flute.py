from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("Flute",)

################################################################################
class Flute(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-173",
            name="Flute",
            description="Get 3 Focus when Absorption is activated.",
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        # If we're a monster
        if isinstance(ctx.target, DMMonster):
            # Receiving the effect of Absorption
            if ctx.status.name == "Absorption":
                # And it will succeed
                if ctx.stacks > 0:
                    # Add 3 Focus
                    ctx.target.add_status("Focus", 3, self)

################################################################################
