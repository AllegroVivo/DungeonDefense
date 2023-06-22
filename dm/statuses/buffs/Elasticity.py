from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Elasticity",)

################################################################################
class Elasticity(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-108",
            name="Elasticity",
            description=(
                "Cancels the next damage to be received by up to 10% of max LIFE. "
                "The stat is reduced by 1 each time damage is received."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.target:
            # Effective for up to 10% of max LIFE.
            effect_value = min(ctx.damage, int(self.owner.max_life * 0.10))
            # Perform the adjustment
            ctx.mitigate_flat(effect_value)
            # And reduce the stat
            self.reduce_stacks_by_one()

################################################################################
