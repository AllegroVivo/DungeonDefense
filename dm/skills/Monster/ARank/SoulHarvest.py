from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SoulHarvest",)

################################################################################
class SoulHarvest(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-250",
            name="Soul Harvest",
            description=(
                "Inflict 32 (+3.0*ATK) damage to an enemy. If the enemy dies "
                "with the attack, recover all allies' life by (2.0*ATK)."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=32, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        if not ctx.target.is_alive:
            for unit in self.room.units_of_type(self.owner):
                unit.heal(self.owner.attack * 2.0)

################################################################################
