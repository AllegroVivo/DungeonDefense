from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Shock",)

################################################################################
class Shock(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-124",
            name="Shock",
            description=(
                "Receive additional damage as much as Shock stat when receiving "
                "damage. The stat is reduced by half each time it is activated."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're defending
        if self.owner == ctx.target:
            # Add damage
            ctx.amplify_flat(self.stacks)

            # Check for Recharge before reducing stacks
            recharge = self.owner.get_status("Recharge")
            if recharge is not None:
                # If present, reduce it instead.
                recharge.reduce_stacks_by_one()
            else:
                # Reduce if Recharge didn't block it.
                self.reduce_stacks_by_half()

################################################################################
