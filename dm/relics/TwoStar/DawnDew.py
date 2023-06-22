from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.monster import DMMonster
################################################################################

__all__ = ("DawnDew",)

################################################################################
class DawnDew(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-170",
            name="Dawn Dew",
            description="Gives 2 Defense when Absorption is given.",
            rank=2,
            unlock=UnlockPack.Original
        )

        # Need to listen for Absorption?

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Absorption":
            if isinstance(ctx.target, DMMonster):
                ctx.target.add_status("Defense", 2, self)

################################################################################
