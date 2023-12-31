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
        """Automatically called upon dispatch of the `on_attack` event."""

        # If a hero is taking the hit, increase damage by 25%
        if isinstance(ctx.target, DMHero):
            obey = ctx.target.get_status("Obey")
            if obey is not None:
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.25

################################################################################
