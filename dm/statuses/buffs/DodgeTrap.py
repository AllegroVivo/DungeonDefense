from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ...core.objects.status import DMStatus
from ...rooms.traproom import DMTrapRoom
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DodgeTrap",)

################################################################################
class DodgeTrap(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-107",
            name="Dodge Trap",
            description="UrMom",
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        # Pretty self-explanatory.
        if ctx.defender == self.owner:
            if isinstance(ctx.attacker, DMTrapRoom):
                ctx.will_fail = True
                self.reduce_stacks_by_one()

################################################################################
