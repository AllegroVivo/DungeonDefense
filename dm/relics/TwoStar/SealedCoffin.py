from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SealedCoffin",)

################################################################################
class SealedCoffin(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-178",
            name="Sealed Coffin",
            description=(
                "Damage inflicted to enemy increases by 100 % when LIFE is "
                "below 10%."
            ),
            rank=2,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're a monster
        if isinstance(ctx.source, DMMonster):
            # Attacking a hero
            if isinstance(ctx.target, DMHero):
                # And our health is below 10%
                if ctx.source.life < ctx.source.max_life * 0.10:
                    # Increase our damage by 100%
                    ctx.amplify_pct(1.00)

################################################################################
