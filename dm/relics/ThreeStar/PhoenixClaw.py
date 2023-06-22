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

__all__ = ("PhoenixClaw",)

################################################################################
class PhoenixClaw(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-223",
            name="Phoenix's Claw",
            description=(
                "Every time a monster attacks an enemy in Burn state, 2 "
                "Acceleration is acquired at a 20 % chance."
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If the attacker is a monster and the defender is a hero...
        if isinstance(ctx.source, DMMonster):
            if isinstance(ctx.target, DMHero):
                # Check if the defender is in Burn state.
                burn = ctx.target.get_status("Burn")
                if burn is not None:
                    # If so, roll a 20 % chance to add 2 Acceleration.
                    if self.random.chance(20):
                        ctx.source.add_status("Acceleration", 2, self)

################################################################################
