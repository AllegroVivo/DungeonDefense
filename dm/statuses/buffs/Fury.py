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
                "The next attack or skill deals additional damage equal to amount "
                "of Fury possessed. The stat is halved upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.attacker == self.owner:
            # Add damage equal to stacks
            ctx.amplify_flat(self.stacks)
            # Reduce if not under the effect of Merciless (prevents Fury reduction)
            merciless = self.owner.get_status("Merciless")
            if merciless is not None:
                merciless -= 1
            else:
                self.reduce_stacks_by_half()

################################################################################
