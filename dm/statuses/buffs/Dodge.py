from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Dodge",)

################################################################################
class Dodge(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-106",
            name="Dodge",
            description=(
                "Evades the next attack. Stat decreases by 1 and you gain 1 "
                "Dodge Resist per evasion."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.defender == self.owner:
            # Check against the resist first.
            resist = self.owner.get_status("Dodge Resist")
            if resist is not None:
                if resist.stacks >= self.stacks:
                    return

            # Basically a dodge.
            ctx.will_fail = True

            # Reduce stacks and apply the antibuff
            self.reduce_stacks_by_one()
            self._parent += self.game.spawn("Dodge Resist", parent=self.owner)

################################################################################
