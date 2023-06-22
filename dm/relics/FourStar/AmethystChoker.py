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

        self.listen("hero_spawn")

################################################################################
    def notify(self, hero: DMHero) -> None:
        """A general event response function."""

        corrupted = [m for m in self.game.deployed_monsters if m.corrupted]
        if not corrupted:
            return

        hero.add_status("Corruption", len(corrupted), self)

################################################################################
