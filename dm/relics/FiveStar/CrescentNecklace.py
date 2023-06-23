from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusExecutionContext
################################################################################

__all__ = ("CrescentNecklace",)

################################################################################
class CrescentNecklace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-317",
            name="Crescent Necklace",
            description="The effect of Vulnerable increases to 300 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_execute")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 2.50  # Base 50% effectiveness to total 300%

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        # If the owner of the status is a hero, increase the effect of the status
        if isinstance(ctx.target, DMHero):
            if ctx.status.name == "Vulnerable":
                ctx.status.increase_base_effect(self.effect_value())

################################################################################
