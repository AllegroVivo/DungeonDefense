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
                "When damaging the next enemy, deals extra damage equal to "
                "Regeneration possessed."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.attacker == self.owner:
            regeneration = self.owner.get_status("Regeneration")
            if regeneration is not None:
                ctx.amplify_flat(int(regeneration.stacks * self.effect_value()))

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **effect = 1 + (n * a)**

        In this function:

        - n is the number of Nature's Power stacks.
        - a is the additional effectiveness per stack.
        """

        return 1 + (self.stacks * 0.005)

################################################################################
