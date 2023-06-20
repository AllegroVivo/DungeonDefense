from __future__ import annotations

import random

from typing import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SecondMarkOfAsceticism",)


################################################################################
class SecondMarkOfAsceticism(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-320",
            name="Second Mark of Asceticism",
            description="The Dark Lord dodges enemy attacks at a 35% chance.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

        self._kills = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If a hero is attacking
        if isinstance(ctx.attacker, DMHero):
            # And the Dark Lord is defending
            if ctx.defender == self.game.dark_lord:
                # 35% chance to dodge
                chance = random.random()
                if chance <= 0.35:
                    # Basically a dodge.
                    ctx.will_fail = True

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.defender, DMHero):
            if ctx.attacker == self.game.dark_lord:
                self._kills += 1

        if self._kills >= 500:
            self.advance_relic()

################################################################################
    def advance_relic(self) -> None:

        # Unsubscribe from the event because the relic is about to be removed
        self.game.unsubscribe_event("on_death", self.notify)
        # Add the specified new relic
        self.game.add_relic("Third Mark of Asceticism")
        # Remove this relic
        self.game.relics.remove_relic(self)

################################################################################
