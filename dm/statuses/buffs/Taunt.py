from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Taunt",)

################################################################################
class Taunt(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-129",
            name="Taunt",
            description="Become all enemies' target.",
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner.room == ctx.room:
            # Force change the defending unit to the owner of this status.
            if self.owner != ctx.defender:
                ctx.reassign_defender(self.owner)

        # Register callback to reduce stacks if damage is actually done
        ctx.register_after_execute(self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.defender:
            if ctx.damage > 0:
                self.reduce_stacks_by_one()

################################################################################
