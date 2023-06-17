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
                "Forces the next enemy attempting to attack this the owner "
                "to attack itself. Stat decreases by 1 and unit gains 1 Mirror "
                "Fragment upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.defender:
            # Change attack target to the attacker
            ctx.reassign_defender(ctx.attacker)

            # Reduce stacks and apply antibuff
            self.reduce_stacks_by_one()
            self.owner.add_status("Mirror Fragment")

################################################################################
