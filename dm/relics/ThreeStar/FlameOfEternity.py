from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("FlameOfEternity",)

################################################################################
class FlameOfEternity(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-220",
            name="Flame of Eternity",
            description=(
                "Enemies under the effect of Burn will receive 15 % more damage."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're attacking a hero
        if isinstance(ctx.target, DMHero):
            # And they have the Burn status
            burn = ctx.target.get_status("Burn")
            if burn is not None:
                # Increase the damage they take by 15%
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.15

################################################################################
