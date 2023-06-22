from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LoopOfFate",)

################################################################################
class LoopOfFate(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-197",
            name="Loop of Fate",
            description=(
                "Inflict 75% additional damage whenever a monster attacks an "
                "enemy with full LIFE."
            ),
            rank=3
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're a monster
        if isinstance(ctx.source, DMMonster):
            # Attacking an enemy
            if isinstance(ctx.target, DMHero):
                # With full life
                if ctx.target.life == ctx.target.max_life:
                    # Increase our damage by 75%
                    ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.75

################################################################################
