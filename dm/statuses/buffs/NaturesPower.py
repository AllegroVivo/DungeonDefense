from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("NaturesPower",)

################################################################################
class NaturesPower(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-119",
            name="Nature's Power",
            description=(
                "When damaging the next enemy, deal extra damage equal to "
                "Regeneration possessed."
            ),
            stacks=stacks,
            status_type=StatusType.Buff,
            base_effect=0.005
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.source:
            ctx.amplify_flat(int(self.effect_value()))

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = b * s**

        In this function:

        - b is the base adjustment.
        - s is the number of Regeneration stacks.
        """

        regeneration = self.owner.get_status("Regeneration")
        if regeneration is None:
            return 0

        return self.base_effect * regeneration.stacks

################################################################################
