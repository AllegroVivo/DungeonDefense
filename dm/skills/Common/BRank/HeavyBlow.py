from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HeavyBlow",)

################################################################################
class HeavyBlow(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-131",
            name="Heavy Blow",
            description=(
                "Inflict 20 (+3.0*ATK) damage and apply 2 Stun to an enemy."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=20, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Apply damage
            ctx.target.damage(self.effect)
            # And inflict Stun
            ctx.target.add_status("Stun", 2, self)

################################################################################
