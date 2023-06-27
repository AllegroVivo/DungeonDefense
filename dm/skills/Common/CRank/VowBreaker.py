from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("VowBreaker",)

################################################################################
class VowBreaker(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-111",
            name="Vow Breaker",
            description=(
                "Inflict 24 (+3.0*ATK) damage and apply 5 Obey to target."
            ),
            rank=1,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=24, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Damage the target
            ctx.target.damage(self.effect)
            # Apply Obey
            ctx.target.add_status("Obey", 5, self)

################################################################################
