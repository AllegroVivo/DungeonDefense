from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("InsigniaOfTerror",)

################################################################################
class InsigniaOfTerror(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-114",
            name="Insignia of Terror",
            description=(
                "Gives 1 Panic to the hero that landed on a trap for the first time."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("trap_activated", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general receptor function for any argument-emitting events."""

        if isinstance(ctx.attacker, DMTrapRoom):
            if isinstance(ctx.defender, DMHero):
                if not ctx.attacker.activated_for_the_first_time:
                    ctx.defender.add_status("Panic")
                    ctx.attacker._activated_first_time = True

################################################################################
