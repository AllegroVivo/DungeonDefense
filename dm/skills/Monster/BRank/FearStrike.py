from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FearStrike",)

################################################################################
class FearStrike(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-215",
            name="Fear Strike",
            description=(
                "Inflict 16 (+3.0*ATK) damage and apply 4 Panic to an enemy. "
                "Deal 5 % extra damage per number of target's Panic stack."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=16, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        panic = ctx.target.get_status("Panic")
        additional = panic.stacks * 0.05 if panic is not None else 0
        ctx.target.damage(self.effect + additional)

################################################################################
