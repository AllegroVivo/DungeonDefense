from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManaCollector",)

################################################################################
class ManaCollector(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-199",
            name="Mana Collector",
            description=(
                "Recover Empty Mana Crystals equal to the number of monsters "
                "deployed at the start of the battle."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("battle_start", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b * m**

        In this function:

        - b is the base adjustment.
        - m is the number of monsters deployed.
        """

        return 1 * len(self.game.deployed_monsters)

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        self.game.dark_lord.restore_mana(int(self.effect_value()))

################################################################################
