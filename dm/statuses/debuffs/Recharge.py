from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Recharge",)

################################################################################
class Recharge(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-122",
            name="Recharge",
            description=(
                "Prevents the reduction of Shock stat 1 time when receiving damage."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

        # Implemented in Shock status logic

################################################################################
