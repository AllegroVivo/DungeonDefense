from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Smash",)

################################################################################
class Smash(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-229",
            name="Smash",
            description=(
                "Inflict 36(+3.0*ATK) damage to the enemy. Inflict 400 % on Armor."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=36, scalar=3.0)
        )

        # Assuming this means that the attack will do 400% damage to units
        # under the effect of the Armor status effect.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        armor = ctx.target.get_status("Armor")
        scalar = 4 if armor is not None else 1
        ctx.target.damage(self.effect * scalar)

################################################################################
