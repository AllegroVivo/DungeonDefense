from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicBlade",)

################################################################################
class MagicBlade(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-105",
            name="Magic Blade",
            description=(
                "Inflict 8 (+3.0*ATK) damage and apply 1 Fragile to an enemy."
            ),
            rank=1,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=8, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Damage the target
            ctx.target.damage(self.effect)
            # Apply Fragile
            ctx.target.add_status("Fragile", 1, self)

################################################################################
