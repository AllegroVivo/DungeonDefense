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
            status_type=DMStatusType.Buff,
            base_effect=0.10
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        ctx.register_after_execute(self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            # If the status owner is going to take damage
            if ctx.damage > 0:
                # Add Fury.
                self.owner.add_status("Fury", stacks=self.effect_value())
                # Reduce stacks
                self.reduce_stacks_by_half()

################################################################################
    @property
    def base_effect(self) -> float:

        return (self._base_effect * self._base_scalar) * self.owner.max_life

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b + (a * s)**

        In this function:

        - b is the base adjustment.
        - a is the additional effectiveness per stack
        - s is the number of Rebound stacks.
        """

        return self.base_effect + (0.01 * self.stacks)

################################################################################
