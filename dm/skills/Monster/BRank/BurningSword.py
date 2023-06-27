from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BurningSword",)

################################################################################
class BurningSword(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-212",
            name="Burning Sword",
            description=(
                "Inflict 21 (+3.0*ATK) damage, and then inflict additional "
                "damage as much as enemy's Burn."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=21, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        burn = ctx.target.get_status("Burn")
        additional = burn.stacks if burn is not None else 0
        ctx.target.damage(self.effect + additional)

################################################################################
