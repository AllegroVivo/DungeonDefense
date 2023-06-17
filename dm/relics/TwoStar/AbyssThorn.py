from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.status import DMStatus

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssThorn",)

################################################################################
class AbyssThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-134",
            name="AbyssThorn",
            description="Doubles Thorn damage against enemies.",
            rank=2
        )

        # Implemented in Thorn calculations.

################################################################################
