from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HealingWind",)

################################################################################
class HealingWind(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-271",
            name="Healing Wind",
            description=(
                "Apply 12 (+1.0*ATK) Regeneration and 2 Shield to all allies "
                "in the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=12, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for monster in self.game.all_monsters:
            monster.add_status("Regeneration", 12 + (1.0 * monster.attack), self)
            monster.add_status("Shield", 2, self)

################################################################################
