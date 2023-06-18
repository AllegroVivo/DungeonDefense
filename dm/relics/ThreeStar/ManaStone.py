from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManaStone",)

################################################################################
class ManaStone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-202",
            name="Mana Stone",
            description="Recover 3 Empty Mana Crystal at the beginning of battle.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("battle_start", self.notify)

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        self.game.dark_lord.restore_mana(3)

################################################################################
