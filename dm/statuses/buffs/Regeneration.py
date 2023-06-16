from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Regeneration",)

################################################################################
class Regeneration(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-125",
            name="Regeneration",
            description=(
                "Recover LIFE equal to Regeneration stats at the start of each action. "
                "Stat is halved with each activation. Cancels Burn, and vice versa."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("status_acquired", self.try_negate_debuff)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        self.owner.heal(self.stacks)
        self.reduce_stacks_by_half()

################################################################################
    def try_negate_debuff(self, status: DMStatus) -> None:

        if status.owner != self.owner:
            return

        if status.name == "Burn":
            # If Burn, we negate at a 1:1 ratio.
            negation = min(self.stacks, status.stacks)

            # Otherwise negate at a 1:All ratio.
            status.reduce_stacks_flat(negation)
            self.reduce_stacks_flat(negation)

            # Reduce and apply resist
            self.owner.add_status("Immune Resist")

################################################################################
