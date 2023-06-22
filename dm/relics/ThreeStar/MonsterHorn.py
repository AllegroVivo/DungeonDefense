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

__all__ = ("MonsterHorn",)

################################################################################
class MonsterHorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-232",
            name="Monster Horn",
            description="Get 1 Merciless from attacking enemies in Stun state.",
            rank=3,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If a hero is being attacked...
        if isinstance(ctx.target, DMHero):
            # By a monster...
            if isinstance(ctx.source, DMMonster):
                # And the monster has the Stun status...
                stun = ctx.target.get_status("Stun")
                if stun is not None:
                    # Add 1 Merciless to the attacker.
                    ctx.source.add_status("Merciless", 1)

################################################################################
