from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ImmuneResist",)

################################################################################
class ImmuneResist(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ABF-103",
            name="Immune Resist",
            description=(
                "Immune cost gradually increases depending on the Immune Resist "
                "owned."
            ),
            stacks=stacks,
            status_type=StatusType.AntiBuff
        )

        # Implemented in Immune status class

################################################################################
