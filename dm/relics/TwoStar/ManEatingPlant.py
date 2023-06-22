from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ManEatingPlant",)

################################################################################
class ManEatingPlant(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-154",
            name="Man-eating Plant",
            description=(
                "Damage that heroes receive from traps increases by 30 % when "
                "the hero's LIFE is low. "
            ),
            rank=2
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're being attacked by a trap
        if isinstance(ctx.source, DMTrapRoom):
            # Check for low health. Not sure what that constitutes in the
            # original, but I'm going to say 30% seems reasonable. May adjust.
            if ctx.target.life < ctx.target.max_life * 0.30:
                # Increase damage.
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################
