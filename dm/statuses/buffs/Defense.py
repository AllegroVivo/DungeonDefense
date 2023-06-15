from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Defense",)

################################################################################
class Defense(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-105",
            name="Defense",
            description=(
                "Damage received is decreased by 50%, with increasing "
                "effectiveness dependent on the number of Defense stacks "
                "possessed. Stat is halved upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

        self.damage: int = 0

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        # If we're defending
        if ctx.defender == self.owner:
            # Cache a reference to the damage so we can use it in the calculation.
            self.damage = ctx.damage
            # Adjust CTX damage.
            ctx.mitigate_pct(self.effect_value())
            # And reduce stacks.
            self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **% = (n * a) + x**

        In this function:

        - x is the base effectiveness
        - n is the number of Defense stacks.
        - a is the additional effectiveness per stack.
        """

        ret = (self.stacks * 0.001) + 0.50
        self.damage = None

        return ret

################################################################################
