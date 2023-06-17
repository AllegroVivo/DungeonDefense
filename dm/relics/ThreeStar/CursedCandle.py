from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CursedCandle",)

################################################################################
class CursedCandle(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-215",
            name="Cursed Candle",
            description=(
                "Enemies under the effect of Panic will receive 30 % more damage."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're attacking a hero
        if isinstance(ctx.defender, DMHero):
            # And they have the Panic status
            panic = ctx.defender.get_status("Panic")
            if panic is not None:
                # Increase the damage dealt by 30%
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################
