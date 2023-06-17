from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("HealingNecklace",)

################################################################################
class HealingNecklace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-147",
            name="Healing Necklace",
            description=(
                "Increases the amount of heals the Dark Lord receives by 25 %."
            ),
            rank=2
        )

        # Implemented in Dark Lord healing calculations.

################################################################################
