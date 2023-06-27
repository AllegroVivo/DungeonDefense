from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BadBreath",)

################################################################################
class BadBreath(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-279",
            name="Bad Breath",
            description=(
                "Inflict 60 (+0.8*ATK) damage and apply 5 Weak and Vulnerable "
                "to all enemies in the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=60, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.effect)
            hero.add_status("Weak", 5, self)
            hero.add_status("Vulnerable", 5, self)

################################################################################
