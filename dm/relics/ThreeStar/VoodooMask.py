from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VoodooMask",)

################################################################################
class VoodooMask(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-213",
            name="Voodoo Mask",
            description="Give 20 Rampage to all monsters when battle starts.",
            rank=3
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("battle_start", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 20.0

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Rampage", self.effect_value())

################################################################################
