from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FuryMace",)

################################################################################
class FuryMace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-194",
            name="Fury Mace",
            description="Fury is decreased by 25 % instead of 50%.",
            rank=3
        )

        # Handled in the Fury status calculations

################################################################################
