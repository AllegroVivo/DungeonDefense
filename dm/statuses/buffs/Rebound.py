from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Rebound",)

################################################################################
class Rebound(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-124",
            name="Rebound",
            description=(
                "Get Fury equal to 10% of LIFE when you next receive damage, with "
                "increasing effect depending on the Rebound stat possessed. Stat "
                "is halved when receiving damage."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

        self.defender_life: int = 0

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if self.owner == ctx.defender:
            # If the status owner is going to take damage
            if ctx.damage > 0:
                # Grab a reference to the health for use in the effect calculation.
                self.defender_life = ctx.defender.max_life
                # Add Fury.
                self.owner.add_status("Fury", stacks=self.effect_value())
                # Reduce stacks
                self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **effect = (L * 0.10) + (n * a)**

        In this function:

        - L is the defender's base max LIFE.
        - n is the number of Rebound stacks.
        - a is the additional effectiveness per stack.
        """

        return (self.defender_life * 0.10) + (self.stacks * 0.01)

################################################################################
