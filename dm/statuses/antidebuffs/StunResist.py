from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import StatusExecutionContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StunResist",)

################################################################################
class StunResist(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ADBF-103",
            name="Stun Resist",
            description=(
                "Stun cost gradually increases depending on the Stun Resist "
                "possessed."
            ),
            stacks=stacks,
            status_type=StatusType.AntiDebuff
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        if self.owner == ctx.target:
            if ctx.status.name == "Stun":
                if self.stacks >= ctx.status.stacks:
                    ctx.will_fail = True

################################################################################
