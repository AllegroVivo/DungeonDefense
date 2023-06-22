from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("MagicSpring",)

################################################################################
class MagicSpring(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-198",
            name="Magic Spring",
            description=(
                "Traps deal 1~30 % random extra damage when they inflict "
                "damage to heroes."
            ),
            rank=3
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If the attacker is a trap room
        if isinstance(ctx.source, DMTrapRoom):
            # And the target is a hero
            if isinstance(ctx.target, DMHero):
                # Amplify the damage by a random amount.
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return self.random.from_range(0.01, 0.30)

################################################################################
