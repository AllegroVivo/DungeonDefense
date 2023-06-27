from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BoxedFear",)

################################################################################
class BoxedFear(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-202",
            name="Boxed Fear",
            description=(
                "Gain 5 Defense and restore LIFE by 100 (+10.0*ATK)."
            ),
            rank=2,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=100, scalar=10),
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        self.owner.heal(self.effect)
        self.owner.add_status("Defense", 5, self)

################################################################################
