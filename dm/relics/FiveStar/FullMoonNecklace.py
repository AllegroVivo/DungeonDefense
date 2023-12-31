from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.status import DMStatus
    from dm.core.contexts import StatusApplicationContext
################################################################################

__all__ = ("FullMoonNecklace",)

################################################################################
class FullMoonNecklace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-315",
            name="Full Moon Necklace",
            description=(
                "Vulnerable effects increases to 150 % and the monster becomes "
                "immune to Vulnerable, reducing the damage it receives by 15 %."
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
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # Monsters gain and additional 15% damage mitigation when under the
        # effects of Vulnerable.
        if isinstance(ctx.target, DMMonster):
            vulnerable = ctx.target.get_status("Vulnerable")
            if vulnerable is not None:
                ctx.mitigate_pct(0.15)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00  # Additional 100% effect

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        # If the owner of the status is a hero, increase the effect of the status
        if isinstance(status.owner, DMHero):
            if status.name == "Vulnerable":
                status.increase_base_effect(self.effect_value())

################################################################################
    @staticmethod
    def status_applied(ctx: StatusApplicationContext) -> None:

        if isinstance(ctx.target, DMMonster):
            # If the status is Vulnerable, fail the action.
            if ctx.status.name == "Vulnerable":
                ctx.will_fail = True

################################################################################
