from __future__ import annotations

from typing     import TYPE_CHECKING

from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from ...core.objects.monster import DMMonster
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusApplicationContext, StatusExecutionContext
################################################################################

__all__ = ("HalfMoonNecklace",)

################################################################################
class HalfMoonNecklace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-316",
            name="Half Moon Necklace",
            description=(
                "Vulnerable effect increases to 200 % and monsters becomes "
                "immune to Vulnerable."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("status_applied", self.status_applied)
        self.listen("status_execute")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.50  # Base 50% effectiveness to total 200%

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:
        """A general event response function."""

        # If the owner of the status is a hero, increase the effect of the status
        if isinstance(ctx.target, DMHero):
            if ctx.status.name == "Vulnerable":
                ctx.status.increase_base_effect(self.effect_value())

################################################################################
    @staticmethod
    def status_applied(ctx: StatusApplicationContext) -> None:

        if isinstance(ctx.target, DMMonster):
            # If the status is Vulnerable, fail the action.
            if ctx.status.name == "Vulnerable":
                ctx.will_fail = True

################################################################################
