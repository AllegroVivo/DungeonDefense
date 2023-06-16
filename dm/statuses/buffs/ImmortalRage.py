from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ImmortalRage",)

################################################################################
class ImmortalRage(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-115",
            name="Immortal Rage",
            description=(
                "The next attack deals 5% extra damage per Immortality stat "
                "possessed, with increasing effect depending on the Immortal Rage "
                "stat possessed. Stat is halved with each attack."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

        self._immortality_count: int = 0

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if ctx.attacker == self.owner:
            immortality = self.owner.get_status("Immortality")
            if immortality is not None:
                self._immortality_count = immortality.stacks
                ctx.amplify_pct(self.effect_value())
                self.reduce_stacks_by_half()

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        **% = b + (n * a)**

        In this function:

        - b is the base effectiveness per stack.
        - n is the number of Immortality stacks.
        - a is the additional effectiveness per stack.
        """

        if not self._immortality_count:
            return 0

        effectiveness = 0.05 + (self._immortality_count * 0.05)
        self._immortality_count = None

        return effectiveness

################################################################################
