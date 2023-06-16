from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Vampire",)

################################################################################
class Vampire(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-131",
            name="Vampire",
            description=(
                "Recover LIFE as much as Vampire stat possessed when attacking "
                "enemy. Stacks are reduced by half upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if self.owner == ctx.attacker:
            # Pretty straightforward
            self.owner.heal(self.stacks)
            self.reduce_stacks_by_half()

################################################################################
