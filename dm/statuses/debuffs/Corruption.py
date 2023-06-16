from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Corruption",)

################################################################################
class Corruption(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-108",
            name="Corruption",
            description=(
                "Damage received increases by 1% per stat. No effect can reduce "
                "or remove this."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        # If we're defending
        if self.owner == ctx.defender:
            # Increase damage
            ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = n * a**

        In this function:

        - n is the number of Corruption stacks.
        - a is the effectiveness per stack.
        """

        return self.stacks * 0.01

################################################################################