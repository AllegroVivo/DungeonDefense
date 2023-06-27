from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ShieldBlock",)

################################################################################
class ShieldBlock(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-139",
            name="Shield Block",
            description=(
                "Gain 5 Defense."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're defending
        if self.owner == ctx.target:
            self.owner.add_status("Defense", 5, self)

################################################################################
