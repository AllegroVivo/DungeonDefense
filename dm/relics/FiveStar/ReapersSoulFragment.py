from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.room import DMRoom
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import ExperienceContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ReapersSoulFragment",)

################################################################################
class ReapersSoulFragment(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-334",
            name="Reaper's Soul Fragment",
            description="EXP acquired by facilities is increased by 10 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("exp_awarded")

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################
    def notify(self, ctx: ExperienceContext) -> None:

        if isinstance(ctx.object, DMRoom):
            ctx.amplify_pct(self.effect_value())

################################################################################
