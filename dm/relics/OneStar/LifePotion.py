from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LifePotion",)

################################################################################
class LifePotion(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-118",
            name="Life Potion",
            description=(
                "Once per battle, resurrects the Dark Lord with 25 % max LIFE "
                "when the Dark Lord receives critical damage."
            ),
            rank=1
        )

        self._used: bool = False

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)
        self.game.subscribe_event("battle_end", self.reset)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If the Dark Lord was killed
        if ctx.target == self.game.dark_lord:
            # Make sure the effect hasn't already been triggered.
            if not self._used:
                # Set the stat directly to avoid triggering a healing event. Just in case.
                self.game.dark_lord._stats._life.current = self.game.dark_lord.max_life * self.effect_value()
                self._used = True

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.25

################################################################################
    def reset(self) -> None:

        self._used = False

################################################################################
