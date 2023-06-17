from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FakeMap",)

################################################################################
class FakeMap(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-144",
            name="Fake Map",
            description="Ignores enemy's Dodge Trap effect at a 25 % chance.",
            rank=2
        )

        # Implemented in Dodge Trap status calculations

################################################################################
