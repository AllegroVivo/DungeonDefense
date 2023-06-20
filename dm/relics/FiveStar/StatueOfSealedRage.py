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

__all__ = ("StatueOfSealedRage",)

################################################################################
class StatueOfSealedRage(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-337",
            name="Statue of Sealed Rage",
            description=(
                "All characters in the dungeon get Fury as much as 10 % of "
                "ATK when attacking. All characters have a very low chance to "
                "attack allies."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

        self._start_day: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self._start_day = self.game.day.current
        self.listen("day_advance")

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # Doesn't apply to traps.
        if isinstance(ctx.attacker, DMTrapRoom):
            return

        # Add Fury to the attacker.
        ctx.attacker.add_status("Fury", ctx.attacker.attack * self.effect_value())

        # Low chance to attack allies. 5% seems reasonable since
        # this relic only persists for 30 days.
        chance = random.random()
        if chance <= 0.05:
            if isinstance(ctx.attacker, DMHero):
                source = ctx.room.heroes
            else:
                source = ctx.room.monsters
            ctx.reassign_defender(random.choice(source))

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################
    def notify(self, day: DMDay) -> None:
        """A general event response function."""

        if day.current - self._start_day >= 30:
            self.game.unsubscribe_event("day_advance", self.notify)
            self.game.add_relic("Statue of Liberated Rage")
            self.game.relics.remove_relic(self)

################################################################################
