from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Rampage",)

################################################################################
class Rampage(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-123",
            name="Rampage",
            description=(
                "Damage to enemy is increased by 2% and damage to self is increased "
                "by 1% per stack."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if self.owner == ctx.attacker:
            ctx.amplify_pct(self.effect_value())
        else:
            ctx.amplify_pct(self.effect_value() / 2)

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **effect = e * n**

        In this function:

        - n is the number of Rampage stacks.
        - e is the effectiveness per stack.
        """

        return 0.02 * self.stacks

################################################################################
