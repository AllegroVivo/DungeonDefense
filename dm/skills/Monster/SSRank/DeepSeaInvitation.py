from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DeepSeaInvitation",)

################################################################################
class DeepSeaInvitation(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-282",
            name="Deep Sea Invitation",
            description=(
                "Inflict 60 (+0.8*ATK) damage, apply 3 Slow, 2 Dull, and "
                "1 Overweight to all enemies in the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=60, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        for hero in self.game.all_heroes:
            hero.add_status("X", 3, self)
            hero.add_status("X", 2, self)
            hero.add_status("X", 1, self)

################################################################################
