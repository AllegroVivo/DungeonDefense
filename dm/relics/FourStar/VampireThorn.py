from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.monster import DMMonster
    from dm.core.contexts import StatusExecutionContext
################################################################################

__all__ = ("VampireThorn",)

################################################################################
class VampireThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-260",
            name="VampireThorn",
            description="Doubles the amount of life recovered from Vampire.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00  # Additional 100%

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        if ctx.status.name == "Vampire":
            if isinstance(ctx.target, DMMonster):
                ctx.status.increase_base_effect(self.effect_value())

################################################################################
