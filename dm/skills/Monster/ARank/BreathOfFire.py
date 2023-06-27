from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BreathOfFire",)

################################################################################
class BreathOfFire(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-237",
            name="Breath of Fire",
            description=(
                "Inflict 24 (+1.5*ATK) damage and apply 36 (+1.5*ATK) Burn "
                "to all enemies in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=24, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        units = self.room.units_of_type(self.owner, inverse=True)
        for unit in units:
            unit.damage(self.effect)
            unit.add_status("Burn", self.effect + 12, self)

################################################################################
