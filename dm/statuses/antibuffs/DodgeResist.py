from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ...core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DodgeResist",)

################################################################################
class DodgeResist(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ABF-102",
            name="Dodge Resist",
            description=(
                "Dodge cost gradually increases depending on the Dodge Resist owned."
            ),
            stacks=stacks,
            status_type=StatusType.AntiBuff
        )

################################################################################
