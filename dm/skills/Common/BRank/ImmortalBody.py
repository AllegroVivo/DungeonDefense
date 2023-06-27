from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import HealingContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ImmortalBody",)

################################################################################
class ImmortalBody(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-132",
            name="Immortal Body",
            description=(
                "All healing effect is doubled if LIFE is below 50%."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_heal")

################################################################################
    def notify(self, ctx: HealingContext) -> None:

        # If we're the one being healed
        if self.owner == ctx.target:
            # If we're below 50% life
            if self.owner.life < self.owner.max_life / 2:
                # Double the healing effect
                ctx.amplify_pct(1.00)  # 100% additional effectiveness

################################################################################
