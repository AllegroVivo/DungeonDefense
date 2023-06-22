from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SwordOfCharm",)

################################################################################
class SwordOfCharm(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-167",
            name="Sword of Charm",
            description=(
                "When an enemy in Charm status attacks another enemy in Charm "
                "status, it deals 100 % extra damage."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("on_attack", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.source, DMHero):
            if isinstance(ctx.target, DMHero):
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00

################################################################################
