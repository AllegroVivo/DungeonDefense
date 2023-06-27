from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("NightmareSpear",)

################################################################################
class NightmareSpear(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-247",
            name="Nightmare Spear",
            description=(
                "Inflict 24 (+3.0*ATK) and apply 1 Stun if the enemy is "
                "in Panic state."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=24, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        stun = ctx.target.get_status("Panic")
        if stun is not None:
            ctx.target.add_status("Stun", 1, self)

################################################################################
