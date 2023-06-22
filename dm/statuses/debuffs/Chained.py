from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Chained",)

################################################################################
class Chained(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-104",
            name="Chained",
            description=(
                "Disables the next normal attack. Stat is reduced by 1 and unit "
                "gain 1 Chained Resist per every action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're attacking (since this is a debuff)
        if self.owner == ctx.source:
            # If we haven't used a skill
            if ctx.type == AttackType.Attack:
                # First check resistance
                resist = self.owner.get_status("Chained Resist")
                if resist is not None:
                    if resist >= self:
                        return

                # The attack will fail.
                ctx.will_fail = True

                # Reduce stacks and add resist.
                self.reduce_stacks_by_one()
                self.owner.add_status("Chained Resist")

################################################################################
