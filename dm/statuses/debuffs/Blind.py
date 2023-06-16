from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Blind",)

################################################################################
class Blind(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-102",
            name="Blind",
            description=(
                "The next attack will always miss. Stat decreases by 1 and you "
                "gain 1 Blind Resist upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if self.owner == ctx.attacker:
            # Check against resist first and return if it exceeds self.stacks.
            resist = self.owner.get_status("Blind Resist")
            if resist >= self:
                return

            # Attack fails (misses)
            ctx.will_fail = True

            # Reduce stacks and apply antidebuff.
            self.reduce_stacks_by_one()
            self.owner.add_status("Blind Resist")

################################################################################
