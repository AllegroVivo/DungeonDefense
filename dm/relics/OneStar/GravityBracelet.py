from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("GravityBracelet",)

################################################################################
class GravityBracelet(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-112",
            name="Gravity Bracelet",
            description=(
                "Enemies under the effect of Obey will receive 25 % more damage."
            ),
            rank=1
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If a hero is taking the hit, increase damage by 25%
        if isinstance(ctx.defender, DMHero):
            ctx.amplify_pct(0.25)

################################################################################
