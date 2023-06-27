from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ShieldBash",)

################################################################################
class ShieldBash(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-107",
            name="Shield Bash",
            description=(
                "Apply 12 (+3.0*ATK) damage to target, and apply additional "
                "damage as much as 100 % of Armor applied to self."
            ),
            rank=1,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=12, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            damage = self.effect
            # Check for Armor
            armor = self.owner.get_status("Armor")
            if armor is not None:
                # If present, increase the damage
                damage += armor.stacks
            # Apply to target
            ctx.target.damage(damage)

################################################################################
