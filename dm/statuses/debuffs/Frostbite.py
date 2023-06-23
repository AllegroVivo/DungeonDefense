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
            status_type=StatusType.Debuff,
            base_effect=0.05
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're defending
        if self.owner == ctx.target:
            # Increase damage:
            ctx.amplify_pct(self.effect_value())
            # Reduce stacks
            self.reduce_stacks_by_half()

################################################################################
    @property
    def base_effect(self) -> float:

        dull = self.owner.get_status("Dull")
        if dull is None:
            return 0

        return (self._base_effect * self._base_scalar) + (0.001 * dull.stacks)

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Slow stacks.
        """

        slow = self.owner.get_status("Slow")
        if slow is None:
            return 0

        return self.base_effect * slow.stacks

################################################################################
