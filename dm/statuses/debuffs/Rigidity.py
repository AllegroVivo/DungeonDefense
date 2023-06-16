from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Rigidity",)

################################################################################
class Rigidity(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-123",
            name="Rigidity",
            description=(
                "Cannot take action for 1 second per Rigidity. Gains Rigidity "
                "Resist each time Rigidity is given."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("status_acquired", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.owner == self.owner:
            if type(status) == type(self):
                self.owner.add_status("Rigidity Resist")

################################################################################
    def effect_value(self) -> float:
        """The value of this status's effect.

        Breakdown:
        ----------
        **effect = a * n**

        In this function:

        - n is the number of Rigidity stacks.
        - a is the action delay per stack.
        """

        return 1.0 * self.stacks

################################################################################
