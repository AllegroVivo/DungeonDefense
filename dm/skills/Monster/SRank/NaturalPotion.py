from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("NaturalPotion",)

################################################################################
class NaturalPotion(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-260",
            name="Natural Potion",
            description=(
                "Apply 36 (+1.8*ATK) Regeneration, 2 Shield to all allies "
                "in the room."
            ),
            rank=5,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=36, scalar=1.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.room.units_of_type(self.owner):
            unit.add_status("Regeneration", self.effect, self)
            unit.add_status("Shield", 2, self)

################################################################################
