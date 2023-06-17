from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LittleCoin",)

################################################################################
class LittleCoin(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-151",
            name="Little Coin",
            description="Acquire 1 Gold(s) when you kill an enemy with a Trap.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_death", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # If a trap is attacking
        if isinstance(ctx.attacker, DMTrapRoom):
            # And a hero was defending
            if isinstance(ctx.defender, DMHero):
                # Add gold
                self.game.inventory.add_gold(1)

################################################################################
