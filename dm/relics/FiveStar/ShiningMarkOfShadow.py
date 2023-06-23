from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusExecutionContext
################################################################################

__all__ = ("ShiningMarkOfShadow",)

################################################################################
class ShiningMarkOfShadow(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-314",
            name="Shining Mark of Shadow",
            description=(
                "Vulnerable effect increases to 150 % and Vulnerable effect "
                "that monster receives decreases to 35 %."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00  # Additional 100% effect

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Vulnerable":
            if isinstance(ctx.target, DMHero):
                ctx.status.increase_base_effect(self.effect_value())
            else:
                ctx.status.reduce_base_effect(0.15)

################################################################################
