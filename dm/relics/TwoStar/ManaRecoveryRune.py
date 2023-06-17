from __future__ import annotations

import random

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManaRecoveryRune",)

################################################################################
class ManaRecoveryRune(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-153",
            name="Mana Recovery Rune",
            description=(
                "Has a 10 % chance to recover 1 Empty Mana Crystal when "
                "defeating an enemy."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.defender, DMHero):
            chance = random.random()
            if chance <= 10:
                self.game.dark_lord.restore_mana(1)

################################################################################
