from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Bloodlust",)

################################################################################
class Bloodlust(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="STAT-104",
            name="Bloodlust",
            description=(
                "When under the effect of Vampire, DEX and ATK are increased by "
                "10%, with increasing effectiveness dependant upon the number of "
                "Bloodlust stacks possessed. Stat is halved upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def stat_adjust(self) -> None:
        """For use in a no-arguments-required situation. This is not automatically
        called."""

        vampire = self.owner.get_status("Vampire")
        if vampire is not None:
            self.owner.increase_stat_pct("dex", self.effect_value())
            self.owner.increase_stat_pct("attack", self.effect_value())
            # Reduce stacks if activated
            self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **% = (n * a) + x**

        In this function:

        - x is the base adjustment.
        - n is the number of Bloodlust stacks.
        - a is the additional effectiveness per stack.
        """

        # Might split this into two functions if the attack increase isn't significant enough.
        return (self.stacks * 0.005) + 0.10

################################################################################
