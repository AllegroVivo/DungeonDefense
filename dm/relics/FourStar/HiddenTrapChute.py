from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.hero import DMHero
from ...rooms.traproom import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("HiddenTrapChute",)

################################################################################
class HiddenTrapChute(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-251",
            name="Hidden Trap Chute",
            description=(
                "When a trap defeats an enemy, it will reactivate if able to "
                "do so."
            ),
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMTrapRoom):
            if isinstance(ctx.target, DMHero):
                ctx.source.reactivate()

################################################################################
