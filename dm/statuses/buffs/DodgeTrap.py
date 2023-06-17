from __future__ import annotations

import random

from typing     import TYPE_CHECKING, Optional

from ...core.objects.status import DMStatus
from ...rooms.traproom import DMTrapRoom
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DodgeTrap",)

################################################################################
class DodgeTrap(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-107",
            name="Dodge Trap",
            description=(
                "Dodges an attack by a trap. Stacks are reduced by 1 per "
                "activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        # If we're defending
        if self.owner == ctx.defender:
            # And being attacked by a trap
            if isinstance(ctx.attacker, DMTrapRoom):
                # Check the associated relic.
                relic = self.game.get_relic("Fake Map")
                if relic is not None:
                    chance = random.random()
                    if chance > 0.25:  # 25% chance to ignore this stat.
                        # If we pass, the attack will fail.
                        ctx.will_fail = True

                # Reduce stacks regardless.
                self.reduce_stacks_by_one()

################################################################################
