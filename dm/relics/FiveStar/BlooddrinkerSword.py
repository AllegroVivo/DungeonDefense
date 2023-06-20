from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BlooddrinkerSword",)

################################################################################
class BlooddrinkerSword(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-297",
            name="Blooddrinker Sword",
            description=(
                "Get 1 Hatred every time the Dark Lord's LIFE is restored by "
                "the effect of Vampire."
            ),
            rank=5
        )

        # Implemented in the Vampire status effect.

################################################################################
