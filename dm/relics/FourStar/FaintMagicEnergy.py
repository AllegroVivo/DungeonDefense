from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FaintMagicEnergy",)

################################################################################
class FaintMagicEnergy(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-262",
            name="Faint Magic Energy",
            description="Acquire 1 permanent mana crystal.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dark_lord.increase_max_mana(1)

################################################################################
