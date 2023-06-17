from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FourLeafClover",)

################################################################################
class FourLeafClover(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-221",
            name="Four-leaf Clover",
            description=(
                "The Regeneration lost when activated is decreased from "
                "50% to 30 %."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

        # Implemented in Regeneration status calculations

################################################################################
