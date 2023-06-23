from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

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
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=12, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Burn", self.effect, self)

################################################################################
