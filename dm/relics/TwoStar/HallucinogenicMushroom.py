from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("HallucinogenicMushroom",)

################################################################################
class HallucinogenicMushroom(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-146",
            name="Hallucinogenic Mushroom",
            description=(
                "The chances of attacking ally due to Haze increases to 60 %."
            ),
            rank=2
        )

        # Chance appears to already be 100%? Going to leave this blank for now.

################################################################################
