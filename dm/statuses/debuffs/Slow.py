from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Slow",)

################################################################################
class Slow(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-125",
            name="Slow",
            description=(
                "DEX is decreased by 50% and effect increases depending on the "
                "Slow possessed. Stat is halved with each action."
            ),
            stacks=stacks,
            status_type=StatusType.Debuff,
            base_effect=0.50
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        # Apply debuff to DEX
        self.owner.reduce_stat_pct("dex", self.effect_value())
        # Reduce stacks
        self.reduce_stacks_by_half()

################################################################################
    @property
    def base_effect(self) -> float:

        base = self._base_effect

        # Check for the associated relic.
        relic = self.game.get_relic("Net")
        if relic is not None:
            base += 0.10  # Relic increases effectiveness to 60%

        return base * self._base_scalar

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **effect = b + (a * n)**

        In this function:

        - b is the base effect amount.
        - n is the number of Slow stacks.
        - a is the additional effectiveness per stack of Slow.
        """

        slow = self.owner.get_status("Slow")
        scalar = 0 if slow is None else slow.stacks

        return self.base_effect + (0.001 * scalar)

################################################################################
