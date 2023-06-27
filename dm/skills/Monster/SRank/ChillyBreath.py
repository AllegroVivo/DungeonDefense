from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ChillyBreath",)

################################################################################
class ChillyBreath(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-255",
            name="Chilly Breath",
            description=(
                "Inflict 16 (+1.2*ATK) damage, apply 3 Slow, and 1 Stun to all enemies in the room."
            ),
            rank=5,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=16, scalar=1.2)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.room.units_of_type(self.owner, inverse=True):
            unit.damage(self.effect)
            unit.add_status("Slow", 3, self)
            unit.add_status("Stun", 1, self)

################################################################################
