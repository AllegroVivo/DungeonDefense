from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Web",)

################################################################################
class Web(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-130",
            name="Web",
            description=(
                "Receives 10% extra damage per Web. When Web stacks 10 or more "
                "times, Web is removed and gets 1 Rigidity."
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
            ctx.amplify_pct(self.effect_value())

            # Then check for 10+ stacks
            if self.stacks >= 10:
                # If present, remove and give debuff
                self.reduce_stacks_flat(10)
                self.owner.add_status("Rigidity")

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = e * s**

        In this function:

        - e is the base effectiveness.
        - s is the number of Web stacks.
        """

        return 0.10 * self.stacks

################################################################################