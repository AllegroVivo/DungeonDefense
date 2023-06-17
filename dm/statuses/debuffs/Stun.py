from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Stun",)

################################################################################
class Stun(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-127",
            name="Stun",
            description=(
                "Unable to take action for 1 turn. Stat decreases by 1 and you "
                "gain 1 Stun Resist per action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're attacking
        if self.owner == ctx.attacker:
            # Check resistance first
            resist = self.owner.get_status("Stun Resist")
            if resist is not None:
                if resist >= self:
                    return

            # Unable to act
            ctx.will_fail = True

            # Reduce stacks and apply resist.
            self.reduce_stacks_by_one()
            self.owner.add_status("Stun Resist")

################################################################################
