from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ...core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import StatusExecutionContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ArmorFragment",)

################################################################################
class ArmorFragment(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ABF-101",
            name="Armor Fragment",
            description=(
                "Armor Fragment owned increases Armor's cost in proportion "
                "to max LIFE."
            ),
            stacks=stacks,
            status_type=StatusType.AntiBuff
        )

        # I don't really understand what this means, so I'll come back to it.

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        pass

################################################################################
