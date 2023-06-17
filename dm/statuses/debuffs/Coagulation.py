from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Coagulation",)

################################################################################
class Coagulation(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-106",
            name="Coagulation",
            description="Prevents Poison stacks from decreasing 1 time.",
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

        # Implemented in Poison status class

################################################################################
