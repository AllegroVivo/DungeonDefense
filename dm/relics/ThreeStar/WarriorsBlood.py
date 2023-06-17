from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.monster import DMMonster
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import ExperienceContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("WarriorsBlood",)

################################################################################
class WarriorsBlood(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-240",
            name="Warrior's Blood",
            description=(
                "Battle EXP earned by monsters is increased by 2 %. Efficiency "
                "is gradually reduced on repeated acquisition."
            ),
            rank=3,
            unlock=UnlockPack.Myth
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("experience_awarded", self.notify)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = b * (0.99^n)**

        In this function:

        - b is the base effectiveness.
        - n is the number of times this relic has been acquired.
        """

        return 0.02 * (0.99 ** self._count)

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMMonster):
            ctx.scale(self.effect_value())

################################################################################
