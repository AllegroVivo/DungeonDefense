from __future__ import annotations

import random

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ThunderBracelet",)

################################################################################
class ThunderBracelet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-182",
            name="Thunder Bracelet",
            description=(
                "Gives 1 Stun at 25 % chance when inflicting damage to an "
                "enemy under Shock effect."
            ),
            rank=2,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're a hero
        if isinstance(ctx.target, DMHero):
            # And the damage is greater than 0
            if ctx.damage > 0:
                # And the defender has the shock status
                shock = ctx.target.get_status("Shock")
                if shock is not None:
                    if shock.stacks > 0:
                        # 25% chance to stun
                        chance = random.random()
                        if chance <= 0.25:
                            # Add 1 stun
                            ctx.target.add_status("Stun", stacks=1)

################################################################################
