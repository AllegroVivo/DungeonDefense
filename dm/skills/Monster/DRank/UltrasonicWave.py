from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("UltrasonicWave",)

################################################################################
class UltrasonicWave(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-199",
            name="Ultrasonic Wave",
            description=(
                "Inflict 12 (+3.0*ATK) damage and apply 1 Rigidity to an enemy."
            ),
            rank=1,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=12, scalar=3.0),
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Rigidity", 1, self)

################################################################################
