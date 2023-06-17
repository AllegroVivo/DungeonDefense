from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("RegenerationOrb",)

################################################################################
class RegenerationOrb(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-122",
            name="Regeneration Orb",
            description=(
                "Restores the Dark Lord's LIFE by 4 % at the end of each battle."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("battle_end", self.notify)

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        self.game.dark_lord.heal(self.game.dark_lord.max_life * self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.04

################################################################################
