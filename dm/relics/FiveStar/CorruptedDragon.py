from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("CorruptedDragon",)

################################################################################
class CorruptedDragon(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-336",
            name="Corrupted Dragon",
            description=(
                "All heroes' combat abilities are reduced by 20 %, and give "
                "5 Panic when a hero enters."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("hero_spawn")

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for hero in self.game.all_heroes:
            hero.reduce_stat_pct("combat", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################
    def notify(self, hero: DMHero) -> None:
        """A general event response function."""

        hero.add_status("Panic", 5, self)

################################################################################
