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
                "When about to receive damage, negates the damage and grants "
                "Thorn equal to ATK."
            ),
            stacks=stacks,
            status_type=StatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if ctx.target == self.owner:
            # Check against the owner's resist first
            resist = self.owner.get_status("Calmness")
            if resist is not None:
                if resist >= self:
                    return

            # Negate the attack
            ctx.will_fail = True
            # Reduce stacks
            self.reduce_stacks_by_one()
            # Apply resulting buff
            self.owner.add_status("Thorn", stacks=self.owner.attack)
            # And resist
            self.owner.add_status("Calmness")

################################################################################
