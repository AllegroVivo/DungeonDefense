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
                "possessed. Stat is halved when receiving damage."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff,
            base_effect=0.50
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        # If we're defending
        if self.owner == ctx.target:
            # Adjust CTX damage.
            ctx.mitigate_pct(self.effect_value())
            # And reduce stacks.
            self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b + (e * s)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per stack.
        - s is the number of Defense stacks.
        """

        ret = self.base_effect + (0.001 * self.stacks)  # 0.1% additional effectiveness

        return ret

################################################################################
