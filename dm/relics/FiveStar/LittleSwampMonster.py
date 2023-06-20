from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("LittleSwampMonster",)

################################################################################
class LittleSwampMonster(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-324",
            name="Little Swamp Monster",
            description="Slow effect that monster gets is reduced to 30 %.",
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

        return 0.20  # 20% reduced effectiveness equals 30%

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if status.name == "Slow":
            if isinstance(status.owner, DMMonster):
                status.reduce_base_effect(self.effect_value())

################################################################################
