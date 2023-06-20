from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CompletedDNA",)

################################################################################
class CompletedDNA(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-308",
            name="Completed DNA",
            description="EXP required for monsters to level up is reduced by 30 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

        # Probably going to implement this whole set in level-up logic.

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