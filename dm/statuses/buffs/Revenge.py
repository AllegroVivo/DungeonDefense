from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Revenge",)

################################################################################
class Revenge(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-126",
            name="Revenge",
            description=(
                "When about to receive damage, negates the damage once and grants "
                "Thorn equal to ATK."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.defender == self.owner:
            # Negate the attack
            ctx.will_fail = True
            # Reduce stacks
            self.reduce_stacks_by_one()
            # Apply resulting buff
            self.owner.add_status("Thorn", stacks=self.owner.attack)

################################################################################
