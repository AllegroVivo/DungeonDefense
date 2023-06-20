from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.status    import DMStatus
################################################################################

__all__ = ("MarkOfShadow",)

################################################################################
class MarkOfShadow(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-313",
            name="Mark of Shadow",
            description="The effect of Vulnerable increases to 150 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

        self._kills: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        # Have to use two different calls since self.listen automatically uses notify().
        self.listen("status_execute")
        self.game.subscribe_event("on_death", self.on_death)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 1.00  # Additional 100% effect

################################################################################
    def notify(self, status: DMStatus) -> None:
        """A general event response function."""

        if isinstance(status.owner, DMHero):
            if status.name == "Vulnerable":
                status.increase_base_effect(self.effect_value())

################################################################################
    def on_death(self, ctx: AttackContext) -> None:

        vulnerable = ctx.defender.get_status("Vulnerable")
        if vulnerable is not None:
            self._kills += 1

        if self._kills >= 1000:
            self.advance_relic()

################################################################################
    def advance_relic(self) -> None:

        # Unsubscribe from events because the relic is about to be removed
        self.game.unsubscribe_event("on_death", self.on_death)
        self.game.unsubscribe_event("status_execute", self.notify)
        # Add the specified new relic
        self.game.add_relic("Shining Mark of Shadow")
        # Remove this relic
        self.game.relics.remove_relic(self)

################################################################################
