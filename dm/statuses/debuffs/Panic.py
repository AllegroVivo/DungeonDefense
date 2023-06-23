from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Panic",)

################################################################################
class Panic(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-119",
            name="Panic",
            description=(
                "Cannot use skills. Stat decreases by 1 and you gain 1 Fear "
                "Resist per action."
            ),
            stacks=stacks,
            status_type=StatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're attacking
        if self.owner == ctx.source:
            # If the attack is a skill
            if ctx.type is AttackType.Skill:
                # Check resistance
                resist = self.owner.get_status("Fear Resist")
                if resist is not None:
                    if resist >= self:
                        return

                # Fail the attack
                ctx.will_fail = True

                # Reduce stacks and apply resist
                self.reduce_stacks_by_one()
                self.owner.add_status("Fear Resist")

################################################################################
