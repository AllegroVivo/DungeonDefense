from __future__ import annotations

import random

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Haze",)

################################################################################
class Haze(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-115",
            name="Haze",
            description=(
                "The next action is executed towards a random target. Stat "
                "decreases by 1 and you gain 1 Haze Resist per action."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # If we're attacking
        if self.owner == ctx.source:
            # Check resist
            resist = self.owner.get_status("Haze Resist")
            if resist is not None:
                if resist >= self:
                    return

            # Get target sources
            monsters = self.owner.room.monsters
            heroes = self.owner.room.heroes

            # Hard set the new attack target
            ctx.reassign_defender(random.choice(monsters + heroes))  # type: ignore

            # Reduce stacks and apply resist.
            self.reduce_stacks_by_one()
            self.owner.add_status("Haze Resist")

################################################################################
