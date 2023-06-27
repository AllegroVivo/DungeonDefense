from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

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
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=4, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Get the appropriate units
        source = ctx.room.units_of_type(self.owner)
        for _ in range(4):  # 3 repeats to make 4 total
            # Select a random target
            target = self.random.choice(source)
            # Damage them
            target.damage(self.effect)

################################################################################
