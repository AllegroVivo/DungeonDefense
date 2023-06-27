from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HellfireClaws",)

################################################################################
class HellfireClaws(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-218",
            name="Hellfire Claws",
            description=(
                "Inflict 24 (+3.0*ATK) damage to an enemy. If the target is "
                "under the effect of Burn, repeat 4 times."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=24, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        burn = ctx.target.get_status("Burn")
        rng = 5 if burn is not None else 1
        for _ in range(rng):
            ctx.target.damage(self.effect)

################################################################################
