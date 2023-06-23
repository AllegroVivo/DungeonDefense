from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Obey",)

################################################################################
class Obey(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-117",
            name="Obey",
            # description=(  # Original text
            #     "Damage received is increased by 15% per Obey. This stat decreased "
            #     "by 1 every time the enemy receives damage, and the enemy that "
            #     "inflicted damage gets Pleasure as much as its ATK."
            # ),
            description=(
                "Damage received is increased 15% per stack of Obey. This stat "
                "is reduced by 1 every time the unit receives damage, and the "
                "opponent that inflicted that damage gets Pleasure as much as "
                "its ATK."
            ),
            stacks=stacks,
            status_type=StatusType.Debuff,
            base_effect=0.15
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're defending
        if self.owner == ctx.target:
            ctx.amplify_pct(self.effect_value())

            # Reduce stacks
            self.reduce_stacks_by_one()

            # Apply buff to opponent
            ctx.source.add_status("Pleasure", stacks=ctx.source.attack)

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Obey stacks.
        """

        return self.base_effect * self.stacks

################################################################################
