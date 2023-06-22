from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Absorption",)

################################################################################
class Absorption(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-101",
            name="Absorption",
            description=(
                "Only take damage equal to 10% of your Maximum LIFE should the "
                "damage exceed that amount. Reduce Absorption by 1 each time "
                "it is activated."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        # If we're defending
        if self.owner == ctx.target:
            # And if the attack's damage will exceed 10% of max LIFE
            if ctx.damage > self.owner.max_life * 0.10:
                # Do a hard override to 10% of LIFE.
                ctx.override_damage(self.owner.max_life * 0.10)
                # And reduce stacks.
                self.reduce_stacks_by_one()

################################################################################
