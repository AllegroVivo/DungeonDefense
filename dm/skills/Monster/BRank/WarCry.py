from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("WarCry",)

################################################################################
class WarCry(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-235",
            name="War Cry",
            description=(
                "Apply 6 (+1.0*ATK) Fury to all allies in the room."
            ),
            rank=3,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=6, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.room.units_of_type(self.owner):
            unit.add_status("Fury", self.effect, self)

################################################################################
