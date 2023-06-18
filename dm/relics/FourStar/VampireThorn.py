from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VampireThorn",)

################################################################################
class VampireThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-260",
            name="VampireThorn",
            description="Doubles the amount of life recovered from Vampire.",
            rank=4
        )

        # Implemented in Vampire status class

################################################################################
