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
                "The next attack's damage increases 15% per Grudge. This stat "
                "decreases by 1 per attack, but Pleasure equal to self ATK is gained."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.attacker == self.owner:
            # Increase damage
            ctx.amplify_pct(self.effect_value())

            # Reduce stacks
            self.reduce_stacks_by_one()

            # Apply Pleasure buff
            self._parent += self.game.spawn(
                "Pleasure", parent=self.owner, stacks=self.owner.attack // 2
            )

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        G = 0.15 * n

        In this function:

        - n is the number of Grudge stacks.
        """

        return 0.15 * self.stacks

################################################################################
