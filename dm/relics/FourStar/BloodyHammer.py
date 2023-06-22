from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("BloodyHammer",)

################################################################################
class BloodyHammer(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-244",
            name="Bloody Hammer",
            description=(
                "Give extra 1(+0.5 per Dark Lord Lv.) Fury when Vampire is given."
            ),
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_applied")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b + (e * l)**

        In this function:

        - b is the base amount of Fury.
        - e is the number of additional stacks.
        - l is the level of the Dark Lord.
        """

        return 1 + (0.50 * self.game.dark_lord.level)

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        # If we've acquired the Vampire status
        if status.name == "Vampire":
            # And the owner is a monster
            if isinstance(status.owner, DMMonster):
                # Add Fury as well
                status.owner.add_status("Fury", self.effect_value(), self)

################################################################################
