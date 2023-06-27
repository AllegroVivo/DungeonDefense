from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwordDance",)

################################################################################
class SwordDance(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-251",
            name="Sword Dance",
            description=(
                "Inflict 9 (+1.0*ATK) damage to all enemies in the room. "
                "Repeat 4 times."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=9, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for _ in range(4):
            for unit in self.room.units_of_type(self.owner, inverse=True):
                unit.damage(self.effect)

################################################################################
