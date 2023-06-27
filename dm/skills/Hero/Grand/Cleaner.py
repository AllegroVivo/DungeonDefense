from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Cleaner",)

################################################################################
class Cleaner(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-361",
            name="Cleaner",
            description=(
                "Inflict 24 (+3.0*ATK) damage to target and remove a random "
                "buff given to target."
            ),
            rank=5,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=24, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Deal damage
            ctx.target.damage(self.effect)
            # Then remove a random buff
            buffs = [
                s for s in ctx.target.statuses
                if s._type in (StatusType.Buff, StatusType.AntiDebuff)
            ]
            if buffs:
                self.random.choice(buffs).deplete_all_stacks()

################################################################################
