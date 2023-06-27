from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BloodyFang",)

################################################################################
class BloodyFang(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-116",
            name="Bloody Fang",
            description=(
                "Inflict 12 (+3.0*ATK) damage to an enemy, and then inflict "
                "additional damage as much as Vampire."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=12, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Damage the target.
            ctx.target.damage(self.effect)
            # Check for Vampire
            vampire = ctx.target.get_status("Vampire")
            if vampire is not None:
                # Damage the target again for an amount equal to the number of
                # Vampire stacks they possess.
                ctx.target.damage(vampire.stacks)

################################################################################
