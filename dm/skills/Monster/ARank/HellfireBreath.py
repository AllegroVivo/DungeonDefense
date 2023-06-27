from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HellfireBreath",)

################################################################################
class HellfireBreath(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-243",
            name="Hellfire Breath",
            description=(
                "Inflict 19 (+1.5*ATK) damage and 18 (+0.75*ATK) Burn to all "
                "enemies in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=19, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        targets = self.room.units_of_type(self.owner, inverse=True)
        for target in targets:
            target.damage(self.effect)
            target.add_status("Burn", 18 + (0.75 * self.owner.attack), self)

################################################################################
