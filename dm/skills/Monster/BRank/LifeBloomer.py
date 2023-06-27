from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LifeBloomer",)

################################################################################
class LifeBloomer(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-220",
            name="Life Bloomer",
            description=(
                "Restore LIFE by 15 (+3.0*ATK) and apply 12 (+2.0*ATK) "
                "Regeneration to an ally."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=15, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        target = self.random.choice(self.room.units_of_type(self.owner))
        target.heal(self.effect)
        target.add_status("Regeneration", 12 + (2.0 * self.owner.attack), self)

################################################################################
