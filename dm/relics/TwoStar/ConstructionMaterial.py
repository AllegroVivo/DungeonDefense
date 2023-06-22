from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.room import DMRoom
from ...core.objects.relic import DMRelic
from utilities import EXPSource

if TYPE_CHECKING:
    from dm.core.contexts   import ExperienceContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ConstructionMaterial",)

################################################################################
class ConstructionMaterial(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-138",
            name="Construction Material",
            description=(
                "Increases EXP granted to a facility through facility "
                "Enhancement by 15 %."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("exp_awarded")

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:
        """A general event response function."""

        # If the target of the experience is a room
        if isinstance(ctx.object, DMRoom):
            # Ensure the EXP is from facility enhancement
            if ctx.source == EXPSource.Battle:
                # Increase experience
                ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.15

################################################################################
