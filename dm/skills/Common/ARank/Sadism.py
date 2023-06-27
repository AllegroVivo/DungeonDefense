from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType


if TYPE_CHECKING:
    from dm.core.contexts   import TortureContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sadism",)

################################################################################
class Sadism(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-167",
            name="Sadism",
            description=(
                "The effect of Torture increases by 15 %."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("torture_start")

################################################################################
    def notify(self, ctx: TortureContext) -> None:

        ctx.amplify_pct(0.15)

################################################################################
