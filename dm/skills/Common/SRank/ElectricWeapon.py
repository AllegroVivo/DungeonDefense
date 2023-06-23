from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect, UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElectricWeapon",)

################################################################################
class ElectricWeapon(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-192",
            name="Electric Weapon",
            description=(
                "Apply 28 (+1*ATK) Shock to target upon inflicting damage."
            ),
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=28, scalar=1),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            ctx.target.add_status("Shock", self.effect, self)

################################################################################
