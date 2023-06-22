from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("InfinitelyRotatingBlade",)

################################################################################
class InfinitelyRotatingBlade(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-294",
            name="Infinitely Rotating Blade",
            description="Doubles damage from traps at 10 % chance.",
            rank=5
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.source, DMTrapRoom):
            if isinstance(ctx.target, DMHero):
                chance = random.random()
                if chance <= 0.10:
                    ctx.amplify_pct(1.00)  # 100% additional damage

################################################################################
