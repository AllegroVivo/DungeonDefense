from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import ExperienceContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PerfectAmberStone",)

################################################################################
class PerfectAmberStone(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-289",
            name="Perfect Amber Stone",
            description="Increases EXP acquired from battle by 30 %.",
            rank=5
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("experience_awarded")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:
        """A general event response function."""

        ctx.amplify_pct(self.effect_value())

################################################################################
