from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CloakOfAuthority",)

################################################################################
class CloakOfAuthority(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-126",
            name="Cloak of Authority",
            description="Increases the Dark Lord's level by 5.",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dark_lord.level_up(5)

################################################################################
