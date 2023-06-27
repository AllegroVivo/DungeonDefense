from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CorpseExplosionSkill",)

################################################################################
class CorpseExplosionSkill(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-256",
            name="Corpse Explosion",
            description=(
                "Inflict 20 (+3.0*ATK) damage and apply 10 (+1.0*ATK) "
                "Corpse Explosion to an enemy."
            ),
            rank=4,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=20, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Corpse Explosion", 10 + (1 * self.owner.attack), self)

################################################################################
