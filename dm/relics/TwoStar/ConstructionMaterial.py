from __future__ import annotations

from typing     import TYPE_CHECKING

from dm.core.objects.room import DMRoom
from ...core.objects.relic import DMRelic

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

        self.game.subscribe_event("experience_awarded", self.notify)

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:
        """A general event response function."""

        if isinstance(ctx.obj, DMRoom):
            ctx.amplify_pct(0.15)

################################################################################
