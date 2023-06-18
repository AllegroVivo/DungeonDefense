from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DungeonIndex",)

################################################################################
class DungeonIndex(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-192",
            name="Dungeon Index",
            description="The next 2 Facilities you acquire will be pre-upgraded.",
            rank=3
        )

        # Will need to implement specifics as I figure out reward logic

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (e * s)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per stack.
        - s is the number of Acceleration stacks.
        """

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################