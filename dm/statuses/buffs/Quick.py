from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Quick",)

################################################################################
class Quick(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-122",
            name="Quick",
            description="DEX is increased by 1% per stack.",
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        self.owner.increase_stat_pct("dex", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **effect = b * n**

        In this function:

        - n is the number of Acceleration stacks.
        - b is the effectiveness per stack.
        """

        return 0.01 * self.stacks

################################################################################
