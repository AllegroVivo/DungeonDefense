from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Grudge",)

################################################################################
class Grudge(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-112",
            name="Grudge",
            description=(
                "The next attack's damage is increased by 15% per stack of Grudge "
                "possessed. This stat decreases by 1 per attack, but Pleasure "
                "equal to own ATK is gained."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff,
            base_effect=0.15
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.source:
            # Increase damage
            ctx.amplify_pct(self.effect_value())

            # Reduce stacks
            self.reduce_stacks_by_one()

            # Apply Pleasure buff
            self.owner.add_status("Pleasure", stacks=self.owner.attack)

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Grudge stacks.
        """

        return self.base_effect * self.stacks

################################################################################
