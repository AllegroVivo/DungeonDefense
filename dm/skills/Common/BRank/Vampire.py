from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("VampireSkill",)

################################################################################
class VampireSkill(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-144",
            name="Vampire",
            description=(
                "Gain 9 (+1.0*ATK) Vampire."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=9, scalar=1)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Appears to be no activation conditions.
        self.owner.add_status("Vampire", self.effect, self)

################################################################################
