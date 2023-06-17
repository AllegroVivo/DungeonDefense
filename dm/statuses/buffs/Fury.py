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
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.attacker:
            # Add damage equal to stacks
            ctx.amplify_flat(self.stacks)
            # Reduce if not under the effect of Merciless (prevents Fury reduction)
            merciless = self.owner.get_status("Merciless")
            if merciless is not None:
                merciless -= 1
            else:
                self.reduce_stacks_by_half()

################################################################################
