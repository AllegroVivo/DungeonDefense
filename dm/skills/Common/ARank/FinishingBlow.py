from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FinishingBlow",)

################################################################################
class FinishingBlow(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-156",
            name="Finishing Blow",
            description=(
                "Inflict 25 (+3.0*ATK) damage to an enemy. Damage inflicted "
                "is doubled if target's LIFE is below 50%."
            ),
            rank=4,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=25, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Check if target's life is below 50%
            if ctx.target.life < ctx.target.max_life / 2:
                # If so, double damage
                ctx.amplify_pct(1.00)  # Additional 100% damage

################################################################################
