from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Vulnerable",)

################################################################################
class Vulnerable(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-128",
            name="Vulnerable",
            description=(
                "Damage received is increased by 50%, and effect increases "
                "depending on the Vulnerable possessed. Stat is halved when "
                "receiving damage. "
            ),
            stacks=stacks,
            status_type=StatusType.Debuff,
            base_effect=0.50
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're defending
        if self.owner == ctx.target:
            # Increase damage
            ctx.amplify_pct(self.effect_value())

            # Reduce stacks
            self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **effect = b + (a * n)**

        In this function:

        - b is the base effect amount.
        - n is the number of Vulnerable stacks.
        - a is the additional effectiveness per stack of Vulnerable.
        """

        return self.base_effect + (0.001 * self.stacks)

################################################################################
