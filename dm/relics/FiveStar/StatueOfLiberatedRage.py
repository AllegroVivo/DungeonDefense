from __future__ import annotations

import random
from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.game.day import DMDay
################################################################################

__all__ = ("StatueOfLiberatedRage",)

################################################################################
class StatueOfLiberatedRage(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-338",
            name="Statue of Liberated Rage",
            description=(
                "All characters in the dungeon get Fury as much as 30 % of "
                "ATK when attacking. All characters have a very low chance to "
                "attack allies."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # Doesn't apply to traps.
        if isinstance(ctx.source, DMTrapRoom):
            return

        # Add Fury to the attacker.
        ctx.source.add_status("Fury", ctx.source.attack * self.effect_value())

        # Low chance to attack allies. 5% seems reasonable like before.
        chance = random.random()
        if chance <= 0.05:
            if isinstance(ctx.source, DMHero):
                source = ctx.room.heroes
            else:
                source = ctx.room.monsters
            ctx.reassign_defender(random.choice(source))

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################
