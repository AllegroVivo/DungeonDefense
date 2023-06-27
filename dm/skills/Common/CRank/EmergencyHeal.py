from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("EmergencyHeal",)

################################################################################
class EmergencyHeal(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-102",
            name="Emergency Heal",
            description="Gain 16 (+5.0*ATK) Regeneration.",
            rank=2,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=16, scalar=5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        self.owner.add_status("Regeneration", self.effect, self)

################################################################################
