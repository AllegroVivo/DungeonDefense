from __future__ import annotations

import random

from typing     import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BeadsOfObedience",)

################################################################################
class BeadsOfObedience(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-275",
            name="Beads of Obedience",
            description=(
                "Heroes that have been damaged by Dark Lord's skill will be "
                "inflicted with Obey at a very low chance."
            ),
            rank=4,
            unlock=UnlockPack.Advanced
        )

        # Chance value is 6%

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_used", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMHero):
            chance = random.random()
            if chance <= 0.06:
                ctx.target.add_status("Obey", 1)

################################################################################
