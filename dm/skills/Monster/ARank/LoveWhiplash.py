from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LoveWhiplash",)

################################################################################
class LoveWhiplash(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-246",
            name="Love Whiplash",
            description=(
                "Inflict 21 (+3.0*ATK) damage and apply 1 Charm to an enemy."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=21, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Charm", 1, self)

################################################################################
