from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.objects.monster import DMMonster
################################################################################

__all__ = ("SoulOrb",)

################################################################################
class SoulOrb(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-177",
            name="Soul Orb",
            description="Get 1 Shield when Immortality is triggered.",
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Immortality":
            if isinstance(ctx.target, DMMonster):
                if not ctx.will_fail:
                    ctx.status.owner.add_status("Shield", 1, self)

################################################################################
