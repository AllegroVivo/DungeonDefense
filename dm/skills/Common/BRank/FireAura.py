from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FireAura",)

################################################################################
class FireAura(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-128",
            name="Fire Aura",
            description=(
                "Apply 12 (+0.8*ATK) Burn to enemies that have attacked you "
                "or received damaged from you."
            ),
            rank=3,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=12, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Register callback if the owner is involved in the attack.
        if self.owner in (ctx.source, ctx.target):
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if ctx.damage > 0:
            # Apply Burn to the appropriate unit.
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Burn", self.effect, self)

################################################################################
