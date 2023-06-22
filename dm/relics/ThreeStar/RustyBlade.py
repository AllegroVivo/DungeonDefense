from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("RustyBlade",)

################################################################################
class RustyBlade(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-205",
            name="Rusty Blade",
            description="Gives 1 Weak to heroes when they enter the dungeon.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMHero) -> None:
        """A general event response function."""

        unit.add_status("Weak", 1, self)

################################################################################
