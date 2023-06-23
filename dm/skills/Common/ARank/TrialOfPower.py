from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TrialOfPower",)

################################################################################
class TrialOfPower(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-171",
            name="UrMom",
            description=(
                "Inflict 30 (+3.0*ATK) damage to an enemy. Apply 2 Weak if "
                "enemy's ATK is lower than monster's ATK."
            ),
            rank=2,
            cooldown=2,
            effect=SkillEffect(base=30, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.target.damage(self.effect)
            if ctx.target.attack < self.owner.attack:
                ctx.target.add_status("Weak", 2, self)

################################################################################
