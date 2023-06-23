from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicArrow",)

################################################################################
class MagicArrow(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-104",
            name="Magic Arrow",
            description=(
                "Inflict 4 (+3.0*ATK) damage to a random enemy. Repeat 3 times."
            ),
            rank=1,
            cooldown=2,
            effect=SkillEffect(base=4, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        source = ctx.room.units_of_type(self.owner)
        for _ in range(4):  # 3 repeats to make 4 total
            target = self.random.choice(source)
            target.damage(self.effect)

################################################################################
