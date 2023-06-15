from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Phantom",)

################################################################################
class Phantom(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-120",
            name="Phantom",
            description="Avoids being the target of the next wide-ranged attack.",
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

        # Not sure what a "wide-ranged attack" is. Will have to revisit this.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        pass

################################################################################
    def activate(self) -> None:
        """For use in a no-arguments-required situation. This is not automatically
        called."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """This function is called automatically when a stat refresh is initiated.
        A refresh can be initiated manually or by the global listener."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect. For example:

        Breakdown:
        ----------
        D = (D0 * 0.5 * (1 + a * n)) / 2

        In this function:

        - D0 is the original dexterity.
        - n is the number of Acceleration stacks.
        - a is the additional effectiveness per stack.
        """

        pass

################################################################################
