from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BraceletOfFury",)

################################################################################
class BraceletOfFury(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-266",
            name="Bracelet of Fury",
            description=(
                "When Dark Lord receives damage, reduce Fury value by 50 % "
                "of damage received instead of losing LIFE."
            ),
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If the defender is the Dark Lord
        if ctx.defender == self.game.dark_lord:
            # And the Dark Lord is under the effect of Fury
            fury = ctx.defender.get_status("Fury")
            if fury is not None:
                # Reduce the Fury stacks by 50 % of the damage received
                fury.reduce_stacks_flat(int(ctx.damage * 0.50))
                # Mark the attack as a failure so it doesn't reduce LIFE.
                ctx.will_fail = True

################################################################################
