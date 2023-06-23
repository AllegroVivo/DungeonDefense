from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

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
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=8, scalar=0.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Shock", self.effect, self)

################################################################################
