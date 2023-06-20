from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.hero import DMHero
################################################################################

__all__ = ("Greenstone",)

################################################################################
class Greenstone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-290",
            name="Greenstone",
            description=(
                "Gives 10(+1.0 added per Dark Lord Lv.) Poison to heroes "
                "that entered the dungeon."
            ),
            rank=5
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("hero_spawn")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (a * l)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - l is the Dark Lord's level.
        """

        return 10 + (1 * self.game.dark_lord.level)

################################################################################
    def notify(self, hero: DMHero) -> None:
        """A general event response function."""

        hero.add_status("Poison", self.effect_value())

################################################################################
