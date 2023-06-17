from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssFlower",)

################################################################################
class AbyssFlower(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-183",
            name="Abyss Flower",
            description="Poison is decreased by 25 %, instead of 50%.",
            rank=2
        )

        # Handled in the Poison status calculations

################################################################################
