from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FrostArrow",)

################################################################################
class FrostArrow(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-130",
            name="Frost Arrow",
            description=(
                "Inflict 14 (+3.0*ATK) damage and apply 2 Slow to an enemy."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=14, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Apply damage
            ctx.target.damage(self.effect)
            # And inflict Slow
            ctx.target.add_status("Slow", 2, self)

################################################################################
