from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import HealingContext
################################################################################

__all__ = ("HealingNecklace",)

################################################################################
class HealingNecklace(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-147",
            name="Healing Necklace",
            description=(
                "Increases the amount of heals the Dark Lord receives by 25 %."
            ),
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_heal")

################################################################################
    def notify(self, ctx: HealingContext) -> None:

        if self.game.dark_lord == ctx.target:
            ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:

        return 0.25

################################################################################
