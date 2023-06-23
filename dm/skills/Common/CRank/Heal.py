from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Heal",)

################################################################################
class Heal(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-103",
            name="Heal",
            description="Recover 15 (+3.0*ATK) LIFE of ally.",
            rank=1,
            cooldown=2,
            effect=SkillEffect(base=15, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        target = self.random.choice(ctx.room.units_of_type(self.owner))
        target.heal(self.effect)

################################################################################
