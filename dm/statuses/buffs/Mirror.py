from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.hero import DMHero
from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Mirror",)

################################################################################
class Mirror(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-118",
            name="Mirror",
            description=(
                "Forces the next enemy attempting to attack you to attack itself. "
                "Stat decreases by 1 and you gain 1 Mirror Fragment per effect "
                "activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.defender == self.owner:
            # Change attack target to the attacker
            ctx._defender = ctx._attacker

            # Reduce stacks and apply antibuff
            self.reduce_stacks_by_one()
            self.owner.add_status("Mirror Fragment")

################################################################################
