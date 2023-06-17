from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Shield",)

################################################################################
class Shield(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-128",
            name="Shield",
            description=(
                "Negates the damage received by self. Stat decreases by 1 and "
                "you gain 1 Inattention per activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if ctx.defender == self.owner:
            # Check against resist and return if it's too high.
            resist = self.owner.get_status("Inattention")
            if resist is not None:
                if resist >= self:
                    return

            # Negate damage
            ctx.will_fail = True

            # Reduce stacks and apply antibuff
            self.reduce_stacks_by_one()
            self.owner.add_status("Inattention")

################################################################################
