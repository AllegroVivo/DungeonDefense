from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("NecklaceOfFocus",)

################################################################################
class NecklaceOfFocus(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-155",
            name="Necklace of Focus",
            description="Increases the effect of Focus to 100 %.",
            rank=2
        )

        # Implemented in focus status calculations.

################################################################################
