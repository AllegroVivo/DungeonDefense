from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
################################################################################

__all__ = ("DarkCube",)

################################################################################
class DarkCube(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-305",
            name="Dark Cube",
            description=(
                "Enemies will receive 75 % more damage and debuffs "
                "(Burn, Poison, Corpse Explosion, Shock) from traps."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

        # Not prepared for this yet. May need an outgoing status effect CTX.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_acquired")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.75

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        pass

################################################################################
