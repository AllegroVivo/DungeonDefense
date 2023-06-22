from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("BlueCoralReef",)

################################################################################
class BlueCoralReef(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-214",
            name="Blue Coral Reef",
            description="Gives 2 Dull to heroes entering the dungeon.",
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMHero) -> None:
        """A general event response function."""

        unit.add_status("Dull", 2, self)

################################################################################
