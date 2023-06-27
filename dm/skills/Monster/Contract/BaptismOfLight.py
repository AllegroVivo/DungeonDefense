from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BaptismOfLight",)

################################################################################
class BaptismOfLight(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-297",
            name="Baptism of Light",
            description=(
                "Inflict 60 (+1.5*ATK) damage to all enemies in the dungeon "
                "and apply them 12 (+1.2*ATK) Shock and 2 Electrical Short."
            ),
            rank=8,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=60, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.effect)
            hero.add_status("Shock", 12 + (1.2 * self.owner.attack), self)
            hero.add_status("Electrical Short", 2, self)

################################################################################
