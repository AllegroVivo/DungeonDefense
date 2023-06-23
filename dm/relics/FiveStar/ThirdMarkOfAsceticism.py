from __future__ import annotations

import random

from typing import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext, BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ThirdMarkOfAsceticism",)

################################################################################
class ThirdMarkOfAsceticism(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-321",
            name="Third Mark of Asceticism",
            description="Earn 1 Hatred per mana consumed by the Dark Lord.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

        self._kills = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")
        self.listen("boss_skill_used", self.apply_status)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If a hero is attacking
        if isinstance(ctx.source, DMHero):
            # And the Dark Lord is defending
            if ctx.target == self.game.dark_lord:
                # 35% chance to dodge
                if self.random.chance(35):
                    # Basically a dodge.
                    ctx.will_fail = True

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMHero):
            if ctx.source == self.game.dark_lord:
                self._kills += 1

        if self._kills >= 1000:
            self.advance_relic()

################################################################################
    def advance_relic(self) -> None:

        # Unsubscribe from the events because the relic is about to be removed
        self.game.unsubscribe_event("on_death", self.notify)
        self.game.unsubscribe_event("boss_skill_used", self.apply_status)
        # Add the specified new relic
        self.game.add_relic("Last Mark of Asceticism")
        # Remove this relic
        self.game.relics.remove_relic(self)

################################################################################
    def apply_status(self, ctx: BossSkillContext) -> None:

        self.game.dark_lord.add_status("Hatred", ctx.mana_cost, self)

################################################################################
