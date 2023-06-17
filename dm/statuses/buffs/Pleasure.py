from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Pleasure",)

################################################################################
class Pleasure(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-121",
            name="Pleasure",
            description=(
                "Changes to Fury when attacking an enemy, and to Regeneration "
                "when receiving damage. Half of Pleasure remains after the change."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        # Apply the appropriate stat
        status = "Fury" if ctx.attacker == self.owner else "Regeneration"
        self.owner.add_status(status, stacks=self.stacks)

        # Reduce stacks, but check for Ecstasy first.
        ecstasy = self.owner.get_status("Ecstasy")
        if ecstasy is not None:
            ecstasy.reduce_stacks_by_one()
            return

        self.reduce_stacks_by_half()

################################################################################
