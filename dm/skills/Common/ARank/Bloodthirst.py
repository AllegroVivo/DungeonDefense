from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Bloodthirst",)

################################################################################
class Bloodthirst(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-147",
            name="Bloodthirst",
            description=(
                "Gain 12 (+1.0*ATK) Vampire and 3 Bloodlust."
            ),
            rank=4,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=12, scalar=1)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        self.owner.add_status("Vampire", self.effect, self)
        self.owner.add_status("Bloodlust", 3, self)

################################################################################
