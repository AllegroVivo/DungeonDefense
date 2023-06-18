from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AssassinsDagger",)

################################################################################
class AssassinsDagger(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-242",
            name="Assassin's Dagger",
            description=(
                "Enemies under the effect of Charm receive 35 % additional damage."
            ),
            rank=4
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.defender, DMHero):
            charm = ctx.defender.get_status("Charm")
            if charm is not None:
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.35

################################################################################
