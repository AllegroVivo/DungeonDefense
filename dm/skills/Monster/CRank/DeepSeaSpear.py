from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DeepSeaSpear",)

################################################################################
class DeepSeaSpear(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-204",
            name="Deep Sea Spear",
            description=(
                "Inflict 24 (+4.0*ATK) damage to an enemy. If the target is "
                "under the effect of Weak, deal double damage."
            ),
            rank=2,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=24, scalar=4),
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            weak = ctx.target.get_status("Weak")
            if weak is not None:
                ctx.amplify_pct(1.00)  # 100% damage increase

################################################################################
