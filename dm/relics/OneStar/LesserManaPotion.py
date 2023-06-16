from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LesserManaPotion",)

################################################################################
class LesserManaPotion(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-117",
            name="Lesser Mana Potion",
            description="Acquire 2 Mana Crystals.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dark_lord.increase_max_mana(2)

################################################################################
