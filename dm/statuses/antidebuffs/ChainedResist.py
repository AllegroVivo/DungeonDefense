from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ChainedResist",)

################################################################################
class ChainedResist(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ADBF-105",
            name="Chained Resist",
            description=(
                "Chained cost gradually increases depending on the Chained "
                "Resist possessed."
            ),
            stacks=stacks,
            status_type=DMStatusType.AntiDebuff
        )

        # Implemented in Chained status class

################################################################################
