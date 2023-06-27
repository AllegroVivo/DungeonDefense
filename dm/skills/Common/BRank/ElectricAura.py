from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElectricAura",)

################################################################################
class ElectricAura(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-126",
            name="Electric Aura",
            description=(
                "Apply 8 (+0.5*ATK) Shock to enemies that have attacked "
                "you or received damaged from you."
            ),
            rank=3,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=8, scalar=0.5)
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # Register callback if the owner is involved in the attack.
        if self.owner in (ctx.source, ctx.target):
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if ctx.damage > 0:
            # Apply Shock to the appropriate unit.
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Shock", self.effect, self)

################################################################################
