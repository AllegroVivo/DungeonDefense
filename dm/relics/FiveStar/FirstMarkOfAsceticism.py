from __future__ import annotations

from typing import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FirstMarkOfAsceticism",)


################################################################################
class FirstMarkOfAsceticism(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-319",
            name="First Mark of Asceticism",
            description="Dark Lord's LIFE, ATK, and DEF are doubled.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

        self._kills = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.game.dark_lord.increase_stat_pct("life", self.effect_value())
        self.game.dark_lord.increase_stat_pct("attack", self.effect_value())
        self.game.dark_lord.increase_stat_pct("defense", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMHero):
            if ctx.source == self.game.dark_lord:
                self._kills += 1

        if self._kills >= 250:
            self.advance_relic()

################################################################################
    def advance_relic(self) -> None:

        # Unsubscribe from the event because the relic is about to be removed
        self.game.unsubscribe_event("on_death", self.notify)
        # Add the specified new relic
        self.game.add_relic("Second Mark of Asceticism")
        # Remove this relic
        self.game.relics.remove_relic(self)

################################################################################
