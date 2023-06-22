from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("OldAltarKey",)

################################################################################
class OldAltarKey(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-263",
            name="Old Altar Key",
            description="Soul storage space is increased by 10.",
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        pass

################################################################################
