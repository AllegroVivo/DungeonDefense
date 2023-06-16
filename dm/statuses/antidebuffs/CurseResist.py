from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CurseResist",)

################################################################################
class CurseResist(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ADBF-101",
            name="Curse Resist",
            description=(
                "Curse cost gradually increases depending on the Curse Resist "
                "possessed."
            ),
            stacks=stacks,
            status_type=DMStatusType.AntiDebuff
        )

        # Implemented in Curse status class

################################################################################
