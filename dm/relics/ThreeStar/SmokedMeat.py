from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("SmokedMeat",)

################################################################################
class SmokedMeat(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-233",
            name="Smoked Meat",
            description=(
                "When Poison is triggered, deal additional damage as much as "
                "20 % of Burn stat."
            ),
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Poison":
            if isinstance(status.owner, DMHero):
                burn = status.owner.get_status("Burn")
                if burn is not None:
                    status.owner.damage(burn.stacks * self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################
