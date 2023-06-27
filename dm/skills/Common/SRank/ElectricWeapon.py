from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, UnlockPack, CooldownType

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
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=28, scalar=1),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage is being applied
        if not ctx.will_fail:
            # Apply Shock as well
            ctx.target.add_status("Shock", self.effect, self)

################################################################################
