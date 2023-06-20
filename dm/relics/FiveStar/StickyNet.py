from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("StickyNet",)

################################################################################
class StickyNet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-323",
            name="Sticky Net",
            description="The effect of Slow increases to 75 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("stat_execute")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.25  # 25% additional effectiveness to equal 75%

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Slow":
            if isinstance(status.owner, DMHero):
                status.increase_base_effect(self.effect_value())

################################################################################
