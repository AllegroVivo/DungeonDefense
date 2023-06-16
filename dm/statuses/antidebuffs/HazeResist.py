from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("HazeResist",)

################################################################################
class HazeResist(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ADBF-102",
            name="Haze Resist",
            description=(
                "Haze cost gradually increases depending on the Haze Resist "
                "possessed."
            ),
            stacks=stacks,
            status_type=DMStatusType.AntiDebuff
        )

        # Implemented in Haze status class

################################################################################
