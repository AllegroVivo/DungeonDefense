from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Thunder",)

################################################################################
class Thunder(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-284",
            name="Thunder",
            description=(
                "Apply 24 (+2.0*ATK) Shock and 2 Recharge to all enemies in "
                "the dungeon, and 1 Stun at 35 % chance."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=24, scalar=2.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            hero.add_status("Shock", 24, self)
            hero.add_status("Recharge", 2, self)
            if self.random.chance(35):
                hero.add_status("Stun", 1, self)

################################################################################
