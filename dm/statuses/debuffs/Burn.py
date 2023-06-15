from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import HealingContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Burn",)

################################################################################
class Burn(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-103",
            name="Burn",
            description=(
                "Negates LIFE recovery effect equal to the next LIFE recovery "
                "stat. LIFE recovery stat decreases as much as the negation. It "
                "cancels Regeneration and vice versa."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

        # I'm redefining this to negate any LIFE recovery and reduce self.stacks on activate.
        # (Basically the Regeneration effect but for all healing)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("unit_healed", self.callback)

################################################################################
    def callback(self, ctx: HealingContext) -> None:

        if ctx.target == self.owner:
            heals_blocked = min(self.stacks, ctx.calculate())
            ctx.modify_flat(heals_blocked)
            self.reduce_stacks_flat(heals_blocked)

################################################################################
