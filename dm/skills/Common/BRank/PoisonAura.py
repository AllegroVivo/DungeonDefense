from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PoisonAura",)

################################################################################
class PoisonAura(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-135",
            name="Poison Aura",
            description=(
                "Apply 9 (+0.6*ATK) Poison to enemies that have attacked "
                "you or received damaged from you."
            ),
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=9, scalar=0.6)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Poison", self.effect, self)

################################################################################
