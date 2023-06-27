from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("VineLassoSingle",)

################################################################################
class VineLassoSingle(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-254",
            name="Vine Lasso",
            description=(
                "Inflict 36 (+3.0*ATK) damage and apply 1 Chained to an enemy."
            ),
            rank=4,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=36, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Chained", 1, self)

################################################################################
