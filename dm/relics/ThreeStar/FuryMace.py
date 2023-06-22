from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core.contexts   import StackReductionContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FuryMace",)

################################################################################
class FuryMace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-194",
            name="Fury Mace",
            description="Fury is decreased by 25 % instead of 50%.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("stacks_reduced")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50  # 50% of 50% is 25%, so 50% - 25% = 25%

################################################################################
    def notify(self, ctx: StackReductionContext) -> None:
        """A general event response function."""

        if ctx.object.name == "Fury":
            if isinstance(ctx.owner, DMMonster):
                ctx.reduce_pct(self.effect_value())  # Reducing effectiveness will reduce the amount of stacks lost.

################################################################################
