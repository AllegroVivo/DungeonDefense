from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("AmethystChoker",)

################################################################################
class AmethystChoker(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-277",
            name="Amethyst Choker",
            description=(
                "For every Corrupted Hero deployed in the dungeon, gives 1 "
                "Corruption to each hero entering the dungeon."
            ),
            rank=4,
            unlock=UnlockPack.Corruption
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("hero_spawn", self.notify)

################################################################################
    def notify(self, hero: DMHero) -> None:
        """A general event response function."""

        # corrupted = self.game.dungeon.corrupted_heroes
        corrupted = 0
        if corrupted is not None:
            hero.add_status("Corruption", corrupted)

################################################################################
