from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Frostbite",)

################################################################################
class Frostbite(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-114",
            name="Frostbite",
            description=(
                "Damage received increases 5% per Slow possessed, and effect "
                "increases depending on Dull possessed. Stat is halved when "
                "receiving damage."
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
            # Increase damage:
            ctx.amplify_pct(self.effect_value())
            # Reduce stacks
            self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = (b + (a * d)) * n**

        In this function:

        - b is the base effectiveness per stack of Slow.
        - d is the number of Dull stacks
        - n is the number of Slow stacks.
        - a is the additional effectiveness per stack of Dull.
        """
        slow = self.owner.get_status("Slow")
        if slow is None:
            return 0

        dull = self.owner.get_status("Dull")
        dull_stacks = 0 if dull is None else dull.stacks

        return (0.05 + (0.005 * dull_stacks)) * slow.stacks

################################################################################
