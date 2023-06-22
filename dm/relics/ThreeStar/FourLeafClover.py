from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.monster import DMMonster
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import StackReductionContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FourLeafClover",)

################################################################################
class FourLeafClover(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-221",
            name="Four-leaf Clover",
            description=(
                "The Regeneration lost when activated is decreased from "
                "50% to 30 %."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("stacks_reduced")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.40  # 40% of 50% is 20%, so 50% - 20% = 30%

################################################################################
    def notify(self, ctx: StackReductionContext) -> None:
        """A general event response function."""

        if ctx.object.name == "Regeneration":
            if isinstance(ctx.object.owner, DMMonster):  # type: ignore
                ctx.reduce_pct(self.effect_value())  # Reducing effectiveness will reduce the amount of stacks lost.

################################################################################
