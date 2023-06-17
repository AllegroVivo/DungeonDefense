from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Starfish",)

################################################################################
class Starfish(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-180",
            name="Starfish",
            description=(
                "Allies under effect of Pleasure will receive 25 % less damage."
            ),
            rank=2,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're a monster
        if isinstance(ctx.defender, DMMonster):
            # And we have the pleasure status
            pleasure = ctx.defender.get_status("Pleasure")
            if pleasure is not None:
                # Reduce incoming damage by 25%
                ctx.mitigate_pct(0.25)

################################################################################
