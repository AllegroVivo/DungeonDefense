from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BaptismOfFire",)

################################################################################
class BaptismOfFire(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-296",
            name="Baptism of Fire",
            description=(
                "Inflict 60 (+0.8*ATK) damage to all enemies in the dungeon "
                "and apply them 24 (+2.0*ATK) Burn and 2 Living Bomb."
            ),
            rank=8,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=60, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.effect)
            hero.add_status("Burn", 24 + (2.0 * self.owner.attack), self)
            hero.add_status("Living Bomb", 2, self)

################################################################################
