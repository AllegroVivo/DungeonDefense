from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Curse",)

################################################################################
class Curse(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-109",
            name="Curse",
            description=(
                "Negates the next buff you receive. Stat decreases by 1 and you "
                "gain 1 Curse Resist per buff negation. Cancels Immune, and "
                "vice versa."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("status_acquired", self.notify)

################################################################################
    def notify(self, status: DMStatus) -> None:

        if status.type is DMStatusType.Buff:
            # Grab the resist info
            resist = self.owner.get_status("Curse Resist")
            if resist >= self:
                return

            # For Immune, we negate at a 1:1 ratio.
            if status.name == "Immune":
                negation = min(self.stacks, status.stacks)
                # Since we'll be reducing self.stacks by more than 1 unit, we need
                # to see if the resist will need to be factored in.
                if resist is not None:
                    negation -= resist.stacks
                reduction = negation
            else:
                negation = status.stacks
                reduction = 1

            # Otherwise negate at a 1:All ratio.
            status.reduce_stacks_flat(negation)
            self.reduce_stacks_flat(reduction)

            # Reduce and apply resist
            self.owner.add_status("Curse Resist")

################################################################################
