from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManaGrail",)

################################################################################
class ManaGrail(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-201",
            name="Mana Grail",
            description=(
                "The Mana Crystals remaining at the end of battle now carry over "
                "to the next day."
            ),
            rank=3
        )

        # Handled in the day advancement logic.

################################################################################
