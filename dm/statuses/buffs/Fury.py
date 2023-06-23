from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Fury",)

################################################################################
class Fury(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-111",
            name="Fury",
            description=(
                "Adds additional damage to an attack or skill equal to Fury "
                "possessed. Fury stacks are halved each time it is activated."
            ),
            stacks=stacks,
            status_type=StatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.source:
            # Add damage equal to stacks
            ctx.amplify_flat(self.stacks)
            # Reduce if not under the effect of Merciless (prevents Fury reduction)
            merciless = self.owner.get_status("Merciless")
            if merciless is not None:
                merciless -= 1
                return

            # Check for the Fury Mace relic (reduces Fury reduction by 50% to 25%)
            relic = self.game.get_relic("Fury Mace")
            self.reduce_stacks_pct(0.50 if relic is None else 0.25)

################################################################################
