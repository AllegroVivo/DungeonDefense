from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StrawberryPudding",)

################################################################################
class StrawberryPudding(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-179",
            name="Strawberry Pudding",
            description=(
                "Dark Lord gets 10(+2.0 added per Dark Lord Lv.) Fury at the "
                "beginning of battle."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("before_battle", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (e * d)**

        In this function:

        - b is the base adjustment.
        - e is the additional effectiveness per level.
        - d is the Dark Lord's current level.
        """

        return 10 + (2 * self.game.dark_lord.level)

################################################################################
    def notify(self) -> None:
        """A general event response function."""

        self.game.dark_lord.add_status("Fury", stacks=self.effect_value())

################################################################################
