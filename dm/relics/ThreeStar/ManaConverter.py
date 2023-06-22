from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManaConverter",)

################################################################################
class ManaConverter(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-200",
            name="Mana Converter",
            description=(
                "Recovers 1 % LIFE per remaining Mana Crystal at the end of "
                "each battle."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("battle_end")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = (b * l) * m**

        In this function:

        - b is the base restorative effect.
        - l is the player's max LIFE.
        - m is the number of Mana Crystals the player has left over.
        """

        return (0.01 * self.game.dark_lord.max_life) * self.game.dark_lord.current_mana

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        self.game.dark_lord.heal(self.effect_value())

################################################################################
