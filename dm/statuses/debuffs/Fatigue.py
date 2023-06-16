from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Fatigue",)

################################################################################
class Fatigue(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-113",
            name="Fatigue",
            description=(
                "DEX is delayed by 1%. No buff or debuff can reduce or remove this."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        self.owner.reduce_stat_pct("dex", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = a * n**

        In this function:

        - n is the number of Fatigue stacks.
        - a is the effectiveness per stack.
        """

        return 0.01 * self.stacks

################################################################################
