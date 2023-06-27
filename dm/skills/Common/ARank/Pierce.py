from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Pierce",)

################################################################################
class Pierce(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-164",
            name="Pierce",
            description=(
                "Inflict 16 (+3.0*ATK) damage to an enemy. Inflict additional "
                "damage as much as half of enemy's DEF."
            ),
            rank=4,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=16, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Add damage equal to half of target's defense
            ctx.amplify_flat(int(self.effect + (ctx.target.defense / 2)))

################################################################################
