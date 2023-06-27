from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ImmortalCharge",)

################################################################################
class ImmortalCharge(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-314",
            name="Immortal Charge",
            description=(
                "Deals 500 (+5.0*ATK) damage to all enemies in the dungeon. "
                "For each enemy killed by this attack, applies 5 Immortality "
                "and 2 Immortal Rage to all monsters."
            ),
            rank=10,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=500, scalar=5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        pre_count = len(self.game.all_heroes)
        for hero in self.game.all_heroes:
            hero.damage(self.effect)

        post_count = len(self.game.all_heroes)
        for _ in range(pre_count - post_count):
            for monster in self.game.all_monsters:
                monster.add_status("Immortality", 5, self)
                monster.add_status("Immortal Rage", 2, self)

################################################################################
