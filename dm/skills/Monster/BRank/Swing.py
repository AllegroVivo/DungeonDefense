from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Swing",)

################################################################################
class Swing(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-231",
            name="Swing",
            description=(
                "Inflict 16 (+2.0*ATK) damage to an enemy. Repeat 3 times."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=16, scalar=2.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for _ in range(3):
            ctx.target.damage(self.effect)

################################################################################
