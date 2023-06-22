from __future__ import annotations

import random
from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SteelBoomerang",)

################################################################################
class SteelBoomerang(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-258",
            name="Steel Boomerang",
            description="The Dark Lord can attack up to 2 enemies simultaneously.",
            rank=4
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if ctx.source == self.game.dark_lord:
            ctx.register_additional_target(random.choice(ctx.room.heroes))

################################################################################
