from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusExecutionContext
################################################################################

__all__ = ("BlackCatStatue",)

################################################################################
class BlackCatStatue(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-264",
            name="Black Cat Statue",
            description=(
                "Acquires Fury equal to 100 % of ATK when Immortality is activated."
            ),
            rank=4,
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
                ctx.target.add_status("Fury", ctx.target.attack * 1.00, self)

################################################################################
