from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from ...rooms.traproom import DMTrapRoom
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Dull",)

################################################################################
class Dull(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-111",
            name="Dull",
            description=(
                "Damage received from traps is increased by 100%. The stat is "
                "reduced by 1 each time it is activated."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        # If we're defending
        if self.owner == ctx.defender:
            # And a trap is attacking
            if isinstance(ctx.attacker, DMTrapRoom):
                # Increase damage by 100%
                ctx.amplify_pct(1.00)
                # Reduce by one
                self.reduce_stacks_by_one()

################################################################################
