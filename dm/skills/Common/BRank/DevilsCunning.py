from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DevilsCunning",)

################################################################################
class DevilsCunning(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-124",
            name="Devil's Cunning",
            description=(
                "Damage inflicted is doubled if target is in Haze state."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.target:
            # The the target is under the effect of Haze
            haze = ctx.target.get_status("Haze")
            if haze is not None:
                # Double the damage
                ctx.amplify_pct(1.00)  # Add 100% damage

################################################################################
