from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FlameArrow",)

################################################################################
class FlameArrow(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-129",
            name="Flame Arrow",
            description=(
                "Inflict 12 (+3.0*ATK) damage and apply 6 (+1.2*ATK) Burn "
                "to an enemy."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=12, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Apply damage
            ctx.target.damage(self.effect)
            # And inflict Burn
            ctx.target.add_status("Burn", 6 + (1.2 * self.owner.attack), self)

################################################################################
