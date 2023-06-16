from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MirrorFragment",)

################################################################################
class MirrorFragment(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="ABF-104",
            name="Mirror Fragment",
            description=(
                "Mirror cost gradually increases depending on stacks of Mirror "
                "Fragment owned."
            ),
            stacks=stacks,
            status_type=DMStatusType.AntiBuff
        )

        # Implemented in Mirror status class

################################################################################
