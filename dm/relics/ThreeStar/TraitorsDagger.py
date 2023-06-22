from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("TraitorsDagger",)

################################################################################
class TraitorsDagger(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-209",
            name="Traitor's Dagger",
            description=(
                "Doubles damage inflicted when a hero attacks another hero."
            ),
            rank=3
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        ctx.register_after_execute(self.callback)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            # If the attacker is a hero and the defender is a hero...
            if isinstance(ctx.source, DMHero):
                if isinstance(ctx.target, DMHero):
                    # Increase the damage by 100%
                    ctx.amplify_pct(self.effect_value())

################################################################################
