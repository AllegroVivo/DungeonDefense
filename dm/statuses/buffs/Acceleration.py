from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ...core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts.attack import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Acceleration",)

################################################################################
class Acceleration(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-102",
            name="Acceleration",
            description=(
                "DEX is increased by 50%, with increasing effectiveness depending "
                "upon the number of Acceleration stacks possessed. Stacks are halved "
                "upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        self.owner.increase_stat_pct("dex", self.effect_value())

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        self.stat_adjust()
        self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **% = (n * a) + x**

        In this function:

        - x is the base adjustment.
        - n is the number of Acceleration stacks.
        - a is the additional effectiveness per stack.
        """

        return (self.stacks * 0.001) + 0.50

################################################################################
