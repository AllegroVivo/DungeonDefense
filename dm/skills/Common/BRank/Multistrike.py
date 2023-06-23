from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Multistrike",)

################################################################################
class Multistrike(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-134",
            name="Multistrike",
            description=(
                "Inflict 6 (+3.0*ATK) damage to an enemy. Repeats 3 times."
            ),
            rank=2,
            cooldown=2,
            effect=SkillEffect(base=6, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            for _ in range(3):
                ctx.target.damage(self.effect)

################################################################################
