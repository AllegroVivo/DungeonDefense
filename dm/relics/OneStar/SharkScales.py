from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SharkScales",)

################################################################################
class SharkScales(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-131",
            name="Shark Scales",
            description=(
                "Damage inflicted to enemies in Stun state increases by 50 %."
            ),
            rank=1,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.target, DMHero):
            stun = ctx.target.get_status("Stun")
            if stun is not None:
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################
