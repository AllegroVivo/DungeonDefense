from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Weak",)

################################################################################
class Weak(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-129",
            name="Weak",
            description=(
                "ATK decreased by 50%, and effect increases depending on the "
                "amount of Weak possessed. Stat is halved with each action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        self.owner.reduce_stat_pct("attack", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b + (a * s)**

        In this function:

        - b is the base effectiveness.
        - n is the number of Weak stacks.
        - a is the additional effectiveness per stack.
        """

        return 0.50 + (0.001 * self.stacks)

################################################################################
