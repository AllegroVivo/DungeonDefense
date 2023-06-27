from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HellfireSkewer",)

################################################################################
class HellfireSkewer(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-219",
            name="Hellfire Skewer",
            description=(
                "Inflict 12 (+3.0*ATK) and apply 36 (+1.5*Lv) Burn to target."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=12, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Burn", 36 + (1.5 * self.owner.level), self)

################################################################################
