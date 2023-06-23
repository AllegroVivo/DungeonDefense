from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, DayAdvanceContext
    from dm.core.game.game import DMGame
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
        if isinstance(ctx.source, DMTrapRoom):
            return

        # Add Fury to the attacker.
        ctx.source.add_status("Fury", ctx.source.attack * self.effect_value(), self)

        # Low chance to attack allies. 5% seems reasonable since
        # this relic only persists for 30 days.
        if self.random.chance(5):
            source = ctx.room.units_of_type(ctx.source)
            ctx.reassign_defender(self.random.choice(source))

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################
    def notify(self, ctx: DayAdvanceContext) -> None:

        if ctx.next_day - self._start_day >= 30:
            self.game.unsubscribe_event("day_advance", self.notify)
            self.game.add_relic("Statue of Liberated Rage")
            self.game.relics.remove_relic(self)

################################################################################
