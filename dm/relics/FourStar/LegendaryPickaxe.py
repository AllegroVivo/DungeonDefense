from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LegendaryPickaxe",)

################################################################################
class LegendaryPickaxe(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-252",
            name="Legendary Pickaxe",
            description="Immediately expands the dungeon.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dungeon.extend_map(self)

################################################################################
