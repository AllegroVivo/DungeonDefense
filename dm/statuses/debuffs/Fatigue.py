from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
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
            status_type=DMStatusType.Debuff,
            base_effect=0.01
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.owner.reduce_stat_pct("dex", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Fatigue stacks.
        """

        return self.base_effect * self.stacks

################################################################################
