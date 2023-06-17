from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StaffOfReign",)

################################################################################
class StaffOfReign(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-207",
            name="Staff of Reign",
            description=(
                "Increases the level of all monsters by 3 when a Dungeon Fate "
                "is selected."
            ),
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("dungeon_fate", self.notify)

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        for monster in self.game.all_monsters:
            monster.level_up(3)

################################################################################
