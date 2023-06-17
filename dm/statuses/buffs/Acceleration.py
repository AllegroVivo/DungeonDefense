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
                "upon the number of Acceleration stacks possessed. Stat is halved "
                "with each action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff,
            base_effect=0.50
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.owner.increase_stat_pct("dex", self.effect_value())

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        self.stat_adjust()
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
        - s is the number of Acceleration stacks.
        """

        return self.base_effect + (0.001 * self.stacks)  # 0.1% additional per stack.

################################################################################
